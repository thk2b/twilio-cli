# sms-cli
Send text messages from the command line using twilio.

The script reads from stdin, from a file or directly from an argument.
Specify your twilio credentials as environment variables as options.

## Usage

```
usage: twilio [-h] [--account ACCOUNT_SID] [--token AUTH_TOKEN] [--from FROM]
              [--msg MSG | --path PATH] [-v | -q]
              to [to ...]

send text messages from the command line

positional arguments:
  to

optional arguments:
  -h, --help            show this help message and exit
  --account ACCOUNT_SID, -a ACCOUNT_SID
                        your twilio account sid. defaults to the
                        TWILIO_ACCOUNT_SID environment variable
  --token AUTH_TOKEN, -t AUTH_TOKEN
                        your twilio auth token. defaults to the
                        TWILIO_AUTH_TOKEN environment variable
  --from FROM, -f FROM  your twilio origin number. defaults to the TWILIO_FROM
                        environment variable
  --msg MSG, -m MSG     a message to be sent. defaults to stdin if -p is not
                        specified
  --path PATH, -p PATH  a path to a file containing the message to be sent.
                        defaults to stdin if -m is not specified
  -v                    verbose output
  -q                    supress output
```

## Examples

```bash
# export environment variables. See usage for alternatives
$ export TWILIO_ACCOUNT_SID=<your account sid>
$ export TWILIO_AUTH_TOKEN=<your auth token>
$ export TWILIO_FROM=<your twilio number>

$ ./twilio -v "+1 234 567 8912" -m "Hello, World"
sending body:
Hello, World
sent sms <message SID> to +1 234 567 8912

# write message to a file
$ echo "Hello, World, but in a file" > message.txt
$ ./twilio -v "+1 234 567 8912" "+1 9876 543 2109" -p message.txt
sending body:
Hello, World, but in a file
sent sms <message SID> to +1 234 567 8912
sent sms <message SID> to +1 9876 543 2109

# reads message from stdin in combination with quiet mode
$ cat message.txt |./twilio -q "+1 234 567 8912" "+1 9876 543 2109"
<message0 SID>
<message1 SID>

```
