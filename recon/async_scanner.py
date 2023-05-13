
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