# CitriXpose
## Description
A python web client made to dynamically dump internal memory, exploiting the CitrixBleed2 CVE-2025-5777 vulnerability. The program uses the aiohttp to send the malicious POST request. It then decodes and saves the returned memory to ```output/output.txt``` as hexedecimal bytes. 

## Installation
Install necessary dependancies
```# pip install -r requirements.txt```

Create a .env file in the root folder with the below field:
```TARGET_URL="vulnerableserver.com"```

Run the application
```# python main.py```
