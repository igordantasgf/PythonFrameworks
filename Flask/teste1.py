from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World, from Flask!"

    return gera_response(200, "usuario", usuario_json)
