import pytest
import socket
import subprocess
import time


def is_port_open(host, port, timeout=1):
    """Check if a given port is open."""
    with soc