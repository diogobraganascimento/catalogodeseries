import os
from catalogodeseries import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators


class FormularioSerie(FlaskForm):
    nome = StringField('Nome da Serie', [validators.DataRequired(), validators.length(min=1, max=50)])
    categoria = StringField('Categoria', [validators.DataRequired(), validators.length(min=1, max=20)])
    plataforma = StringField('Plataforma', [validators.DataRequired(), validators.length(min=1, max=30)])
    resumo = StringField('Sinopse', [validators.DataRequired(), validators.length(min=20, max=250)])
    c_etaria = StringField('Faixa Etária', [validators.DataRequired(), validators.length(min=1, max=2)])
    nota = StringField('Nota', [validators.DataRequired(), validators.length(min=1, max=1)])
    salvar = SubmitField('Salvar')


class FormularioUsuario(FlaskForm):
    nickname = StringField('Nickname', [validators.DataRequired(), validators.length(min=1, max=8)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.length(min=1, max=100)])
    login = SubmitField('Login')


def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo

    return 'capa_padrao.jpg'


def deleta_arquivo(id):
    arquivo = recupera_imagem(id)
    if arquivo != 'capa_padrao.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH']), arquivo)
