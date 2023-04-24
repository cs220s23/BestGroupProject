"""
Collects covid data to be used within the web server and stored in a redis database
"""
import time
import os
import requests
import redis
import dotenv

dotenv.load_dotenv()

host = os.getenv('REDIS_HOST')
port = os.getenv('REDIS_PORT')

r = redis.Redis(host=host, port=port)

while True:
    url = 'https://data.cdc.gov/resource/9mfq-cb36.json'
    results = requests.get(url).json()

    confirmed = sum([int(result['tot_cases']) for result in results])

    r.set('confirmed', confirmed)
    # Flush the buffer to ensure it is printed immediately
    print(f'Saved {confirmed}. Sleeping for 15 minutes', flush=True)
    time.sleep(15 * 60)
