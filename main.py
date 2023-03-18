import argparse

from orchestration.pentest import PenetrationTester
from webapp.app import app


def main(targets, top_ports):
    pentester = PenetrationTester(targets, top_ports)
    pentester.scan_and_report()
  