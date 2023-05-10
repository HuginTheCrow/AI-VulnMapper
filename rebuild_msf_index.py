
"""
This module provides functionality to build an index of exploits found in the specified directory.
It will search for Ruby files, parse the exploit's name and description, and save the data to a JSON index file.
"""

import os
import re
import json

from config import EXPLOITS_DIR, MSF_INDEX_FILE
