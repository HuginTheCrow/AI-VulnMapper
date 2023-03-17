import argparse

from orchestration.pentest import PenetrationTester
from webapp.app import app


def main(targets, top_ports):
    pentester = PenetrationTester