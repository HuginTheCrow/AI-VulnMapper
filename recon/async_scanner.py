
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
