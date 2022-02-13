"""

An event loop — or main loop, is the central control aspect — is a construct
within programs that controls and dispatches events following an initial event.

"""

from select import select
import sys

message = ""

while True:
    # Listen on events from stdin and  stdout
    #   if event don't appear within 1sec, stop
    #   listening.
    input_fd, output_fd, _ = select([sys.stdin], [sys.stdout], [], 1)

    for event_source in input_fd + output_fd:

        if event_source is sys.stdin:

            message = sys.stdin.readline()

        elif event_source is sys.stdout:
            # Execute only when message is not ""
            if message:
                # Print message
                sys.stdout.write(message)

                sys.stdout.flush()
                # Delete message content
                message = ""
