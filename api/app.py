from flask import Flask
from redis_client import create_redis_record
app = Flask(__name__)

@app.route('/')
def hello():
    name = "Hello World"
    return name

@app.route('/good')
def good():
    name = "Good"
    return name

@app.route('/<key>/<value>')
def create_resource(key, value):
    m = create_redis_record(key=key, value=value)
    return m

if __name__ == "__main__":
    app.run(debug=True)