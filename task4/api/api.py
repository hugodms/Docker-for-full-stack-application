from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/foo": {"origins": "http://127.0.0.1:8080"}})

@app.route("/")
@cross_origin(origin='127.0.0.1',headers=['Content- Type','Authorization'])
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)