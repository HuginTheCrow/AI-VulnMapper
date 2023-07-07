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


def test_server_