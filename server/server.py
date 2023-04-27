import os
import redis
import dotenv
from flask import Flask




app = Flask(__name__)
dotenv.load_dotenv()

host = os.getenv('REDIS_HOST')
port = os.getenv('REDIS_PORT')

r = redis.Redis(host=host, port=port) # type: ignore

def read_count():

    try:
        with open('data/count.txt', 'r') as f:
            count = int(f.read())
        return count
    except IOError:
        return 0

def save_count(count):
    # ensure the directory exists
    os.makedirs('data', exist_ok=True)
    with open('data/count.txt', 'w') as f:
        f.write(str(count))

@app.route("/")
def home():
    confirmed = int(r.get('confirmed')) # type: ignore
    count = read_count() 
    count += 1
    save_count(count)
	
    return f"<h1 style='font-size:{count}vw'>confirmed: {confirmed}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
