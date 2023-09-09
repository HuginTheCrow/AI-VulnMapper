import pytest
import socket
import subprocess
import time


def is_port_open(host, port, timeout=1):
    """Check if a given port is open."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            s.connect((host, port))
            return True
        except socket.error:
            return False


def test_server_start():
    """
    Test the startup of the server by running a Python script in the background.

    The test performs the following steps:
    1. Initiates the server by running 'main.py' script with '127.0.0.1' as an argument.
    2. Waits for an initial duration to account for any startup delay.
    3. Checks for 60 seconds to see if the server starts and becomes accessible on '127.0.0.1:1337'.
    4. If the server starts within the duration, t