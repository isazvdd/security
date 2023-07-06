#!/usr/bin/python

import sys
import socket

USAGE = """\
Verify the state of a TCP port of a Host.

{} <host> <port>
  <host> - the URL or IP address of the Host.
  <port> - the TCP port of the Host.\
"""

if __name__ == "__main__":
    """
    """
    if len(sys.argv) == 3:
        host = sys.argv[1]
        port = int(sys.argv[2])
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            s.connect((host, port))
            print(host, port, "open")
        except ConnectionRefusedError:
            print(host, port, "closed")
        except (TimeoutError, socket.timeout):
            print(host, port, "filtered")
        except Exception as e:
            print(host, port, "?", e)
    else:
        print(USAGE.format(sys.argv[0]))