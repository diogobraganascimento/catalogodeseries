from catalogodeseries import db


class Series(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(20), nullable=False)
    plataforma = db.Column(db.String(30), nullable=False)
    resumo = db.Column(db.String(250), nullable=False)
    c_etaria = db.Column(db.Integer, nullable=False)
    nota = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


class Usuarios(db.Model):
    nickname = db.Column(db.String(8), primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome
