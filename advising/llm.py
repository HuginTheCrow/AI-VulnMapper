
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
        self.title = title
        self.exploits = exploits
        self.api_key = api_key
        self.api_url = api_url
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
        }
        self.logger = Logger(__name__).get_logger()

    def _query_api(self, json_data: Dict) -> str:
        """
        Private method to query the OpenAI API with provided JSON data.

        Args:
            json_data (dict): JSON data to be sent to the API.

        Returns:
            str: Response from the API.
        """

        async def _send_to_openai_async():
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    url=self.api_url,
                    json=json_data,
                    headers=self.headers,
                    timeout=120,
                )
                if response.status_code == 200:
                    return response.json()["choices"][0]["message"]['content']
                else:
                    response.raise_for_status()