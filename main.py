import argparse

from orchestration.pentest import PenetrationTester
from webapp.app import app


def main(targets, top_ports):
    pentester = PenetrationTester(targets, top_ports)
    pentester.scan_and_report()
    app.run(debug=False, host='0.0.0.0', port=1337)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(descri