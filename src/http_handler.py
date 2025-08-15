import aiohttp
from aiohttp_socks import ProxyConnector
from src.request_configuration import *

class CitrixConnection:
    def __init__(self, domain:str, session: aiohttp.ClientSession):
        self.session = session

    async def target(self, proxy:str = None):
        self.proto = "https://"
        self.domain = self.domain
        self.endpoint = "/p/u/doAuthentication.do"

        url = self.proto + self.domain + self.endpoint
        post_body = {"login"}

        async with self.session.post(url, data=post_body, proxy=proxy) as resp:
            text = await resp.text()
            return resp.status, text





