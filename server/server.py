"""
This is the server.py function, which sets up the server
"""
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
    """
    This is the read count function which reads the count from the file, and returns the count,
    when the file is not there, it sets the count to 0.
    """
    try:
        with open('data/count.txt', 'r',encoding="utf-8") as j:
            count = int(j.read())
        return count
    except IOError:
        return 0

def save_count(count):
    """
    This is the save count function, which saves a count to a file
    """
    # ensure the directory exists
    os.makedirs('data', exist_ok=True)
    with open('data/count.txt', 'w',encoding="utf-8") as i:
        i.write(str(count))

@app.route("/")
def home():
    """
    This is the home function.
    """
    confirmed = int(r.get('confirmed')) # type: ignore
    count = read_count()
    count += 1
    save_count(count)

    return f"<h1 style='font-size:{count}vw'>confirmed: {confirmed}</h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
