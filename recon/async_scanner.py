
import json
import multiprocessing
import time
from typing import List, Dict
from utils.logger import Logger
import nmap

from config import COMMON_PORTS


class NetworkScanner:
    """
    Сlass for performing network scans using nmap.
    """

    def __init__(self, target_subnets: List[str], top_ports=300):
        self.target_subnets = target_subnets
        self.top_ports = top_ports
        self.ports = NetworkScanner._load_common_ports(COMMON_PORTS)
        self.results_queue = multiprocessing.Queue()
        self.logger = Logger(__name__).get_logger()

    @staticmethod
    def _load_common_ports(common_ports_file: str) -> List[str]:
        with open(common_ports_file) as f:
            return json.load(f)

    def extract_port_info(self, scanned_host: str, protocol_type: str, port_number: int, scan_data: Dict) -> Dict:
        """
        Extracts information for a scanned port.

        Args:
            scanned_host (str): IP address of the scanned host.
            protocol_type (str): Protocol type, e.g., 'tcp'.
            port_number (int): Port number being scanned.
            scan_data (dict): Scan data returned from nmap scan.

        Returns:
            dict: A dictionary containing port information.
        """
        self.logger.info(f"Extracting port info for {scanned_host}, {protocol_type}, {port_number}")
        protocol_data = scan_data[protocol_type][port_number]
        port_info = {'host': scanned_host, 'protocol': protocol_type, 'port': port_number}
        if protocol_data['state'] != 'open':
            return None
        for key in ['name', 'product', 'version', 'script']:
            if key in protocol_data:
                port_info[key] = protocol_data[key]

        return port_info