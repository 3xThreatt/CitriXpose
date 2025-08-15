REQUESTS_PER_SECOND = 10  
MAX_RETRIES = 3
RETRY_STATUS_CODES = [429, 500, 502, 503, 504]
RATE_LIMIT_DELAY = 2 # sets delay after recieving a retry status code
THROTTLE_DELAY = 0.1 # additional throttle
