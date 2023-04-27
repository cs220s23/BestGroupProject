from flask import Flask
import redis
import dotenv
import os

app = Flask(__name__)
dotenv.load_dotenv()

host = os.getenv('REDIS_HOST')
port = os.getenv('REDIS_PORT')

r = redis.Redis(host=host, port=port)


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
    confirmed = int(r.get('confirmed'))
    count = read_count()    
    count += 1
    save_count(count);
    return "<h1 style='color:green; font-size:{}vw'>confirmed:{}</h1>".format(count,confirmed)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8000)
