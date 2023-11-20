from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from response import gera_response


PASSWORD = os.environ.get('POSTGRES_PASSWORD')

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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


# Selecionar Tudo
@app.route("/comentarios", methods=["GET"])
def seleciona_comentarios():
    comentarios_objetos = Comentarios.query.all()
    comentarios_json = [comentario.to_json() for comentario in comentarios_objetos]

    return gera_response(200, "comentarios", comentarios_json)