from flask import Flask, Response
from flask_sqlalchemy import SQLAlchemy
import json, os
from flask_cors import cross_origin,CORS

PASSWORD = os.environ.get('POSTGRES_PASSWORD')

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://default:{}@ep-autumn-dream-20888543.us-east-1.postgres.vercel-storage.com:5432/verceldb'.format(PASSWORD)
db = SQLAlchemy(app)
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})
app.config['CORS_HEADERS'] = 'Content-Type'

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

# Selecionar Tudo
@app.route("/comentarios", methods=["GET"])
@cross_origin()
def seleciona_usuarios():
    mensagens_objetos = Comentarios.query.all()
    mensagens_json = [mensagem.to_json() for mensagem in mensagens_objetos]

    return gera_response(200, "mensagens", mensagens_json)


# JSON Return
def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if(mensagem):
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")