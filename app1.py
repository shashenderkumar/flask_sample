from flask import Flask

app = Flask(__name__)

@app.route("/")
def haello():
    return "Hello world from app1 script and haello function .. how are you doing .. bhaalu"

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port=5000)