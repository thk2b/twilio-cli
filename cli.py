import os
import sys
import argparse
from twilio.rest import Client

class DefaultEnv(argparse.Action):
    """An argument Action that defaults to an environment variable
    """
    def __init__(self, env, required=True, default=None, help="", **kwargs):
        if not default:
            default = os.getenv(env)
        if required and default:
            required = False
        help = "{}{}defaults to the {} environment variable".format(
            help, ". " if len(help) else "", env)
        super().__init__(required=required, default=default, help=help, **kwargs)

    def __call__(self, parser, namespace, values, optstr=None):
        setattr(namespace, self.dest, values)

def get_args(from_module=False):
    parser = argparse.ArgumentParser(
        description="send text messages from the command line",
    )
    parser.add_argument(
        "--account", "-a",
        dest="account_sid",
        action=DefaultEnv,
        env="TWILIO_ACCOUNT_SID",
        required=True,
        help="your twilio account sid"
    )
    parser.add_argument(
        "--token", "-t",
        dest="auth_token",
        action=DefaultEnv,
        env="TWILIO_AUTH_TOKEN",
        required=True,
        help="your twilio auth token"
    )
    parser.add_argument(
        "--from", "-f",
        dest="from_",
        metavar="FROM",
        action=DefaultEnv,
        env="TWILIO_FROM",
        required=True,
        help="your twilio origin number"
    )
    parser.add_argument(
        "to",
        nargs="+"
    )
    body = parser.add_mutually_exclusive_group()
    body.add_argument(
        "--msg", "-m",
        action="store",
        type=str,
        required=False,
        help="a message to be sent. defaults to stdin if -p     is not specified"
    )
    body.add_argument(
        "--path", "-p",
        action="store",
        type=str,
        required=False,
        help="a path to a file containing the message to be sent. defaults to stdin if -m is not specified"
    )
    return parser.parse_args(sys.argv[1:])

def get_body(args):
    """Return the body of the message based on the arguments
    """
    if args.msg:
        return args.msg
    if args.path:
        try:
            with open(args.path, "r") as file:
                return "".join(file.readlines())
        except FileNotFoundError as e:
            print("error: file not found: {}".format(args.path))
            sys.exit(1)
    return "".join(sys.stdin.readlines())

def send_sms(args):
    body = get_body(args)
    client = Client(args.account_sid, args.auth_token)
    for destination in args.to:
        try:
            message = client.messages.create(
                to=destination, 
                from_=args.from_,
                body=body
            )
            print("sent sms {} to {}".format(message.sid, destination))
        except Exception as e:
            print("error sending to {}: {}".format(destination, e))

if __name__ == "__main__":
    args = get_args(from_module=True)
    send_sms(args)
