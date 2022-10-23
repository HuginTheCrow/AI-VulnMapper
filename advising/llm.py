
import asyncio
import json
import os
from yaml import safe_load
from typing import Dict
from config import PROMPTS_FILE
import httpx

from utils.logger import Logger
from constants import AdvisorConstants

class Advisor:
    """
    Advisor class that prepares the reports by summarizing discoveries and providing attack advice,
    leveraging GPT-4 models from OpenAI API.
    """

    def __init__(self,
                 discovery_result,
                 title,
                 exploits,
                 api_key=os.getenv('OPENAI_API_KEY'),
                 api_url='https://api.openai.com/v1/chat/completions'):
        
        if not (api_key):
            self.logger.error(AdvisorConstants.API_KEY_ERROR)
            while not (api_key):
                api_key = input("PLEASE ENTER OPENAI API KEY: ")
        self.full_discovery_result = discovery_result
        self.discovery_result = " ".join(discovery_result.split()[:2000])