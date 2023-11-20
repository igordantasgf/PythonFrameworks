from flask import Flask, Response
from flask_sqlalchemy import SQLAlchemy
import json, os

PASSWORD = os.environ.get('POSTGRES_PASSWORD')

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://default:{}@ep-autumn-dream-20888543.us-east-1.postgres.vercel-storage.com:5432/verceldb'.format(PASSWORD)
db = SQLAlchemy(app)

# models
class Comentarios(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    mensagem = db.Column(db.String(60))

    def to_json(self):
        return {"mensagem": self.mensagem}


@app.route("/")
def home():
    return "Hello World, from Flask!"

@app.route("/login")
def login():
    return "Login realizado"


# JSON Return
def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if(mensagem):
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")