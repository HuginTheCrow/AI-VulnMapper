
"""
This module provides functionality to build an index of exploits found in the specified directory.
It will search for Ruby files, parse the exploit's name and description, and save the data to a JSON index file.
"""

import os
import re
import json

from config import EXPLOITS_DIR, MSF_INDEX_FILE


def build_index(exploits_dir=EXPLOITS_DIR) -> None:
    """
    Parses and indexes the Name and Description from Ruby (.rb) exploit files located in the specified directory.
    Saves the indexed data as a JSON file (`MSF_INDEX_FILE`).
    The indexing will go through each Ruby file, extract the exploit's name and description, and add this information 
    to the index, along with the relative path to the exploit.
    
    Args:
        exploits_dir (str): The path to the directory containing the Ruby exploit files. Defaults to `EXPLOITS_DIR` from config.
    Returns:
        None
    """
    index = []
    name_pattern = re.compile(r"'Name'\s*=>\s*'([^']*)'", re.IGNORECASE)
    description_pattern = re.compile(r"'Description'\s*=>\s*%q\{([^\}]*)\}", re.IGNORECASE | re.DOTALL)

    for foldername, _, filenames in os.walk(exploits_dir):
        for filename in filenames: