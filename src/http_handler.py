import aiohttp
from aiohttp_socks import ProxyConnector
from src.request_configuration import *

class CitrixConnection:
    def __init__(self, domain:str, session: aiohttp.ClientSession):
        self.session = session
        self.domain = domain
        
    async def target(self):
        self.proto = "https://"
        self.endpoint = "/p/u/doAuthentication.do"
        url = self.proto + self.domain + self.endpoint
        headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:141.0) Gecko/20100101 Firefox/141.0"
}


        async with self.session.post(url, data="login", headers=headers) as resp:
            text = await resp.text()
            return text





