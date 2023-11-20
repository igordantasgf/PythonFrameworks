from main import db

# models
class Comentario(db.Model):
    mensagem = db.Column(db.String(60))

    def to_json(self):
        return {"mensagem": self.mensagem}