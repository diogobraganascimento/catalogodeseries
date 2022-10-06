from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from catalogodeseries import app, db
from models import Series
from helpers import recupera_imagem, deleta_arquivo, FormularioSerie
import time


@app.route('/')
def index():
    return render_template('index.html', titulo='Bem vindo ao Catalogo de Series')


@app.route('/lista')
def lista():
    lista = Series.query.order_by   (Series.id)
    return render_template('lista.html', titulo='Series', series=lista)


@app.route('/detalhe/<int:id>')
def detalhe(id):
    serie = Series.query.filter_by(id=id).first()
    capa_serie = recupera_imagem(id)
    return render_template('detalhe.html', titulo=f'Titulo: {serie.nome}', serie=serie, capa_serie=capa_serie)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    form = FormularioSerie()
    return render_template('novo.html', titulo='Nova Serie', form=form)


@app.route('/criar', methods=['POST', ])
def criar():
    form = FormularioSerie(request.form)

    if not form.validate_on_submit():
        return redirect(url_for('novo'))

    nome = form.nome.data
    categoria = form.categoria.data
    plataforma = form.plataforma.data
    resumo = form.resumo.data
    c_etaria = form.c_etaria.data
    nota = form.nota.data

    serie = Series.query.filter_by(nome=nome).first()

    if serie:
        flash('Serie já existente!')
        return redirect(url_for('lista'))

    nova_serie = Series(
        nome=nome,
        categoria=categoria,
        plataforma=plataforma,
        resumo=resumo,
        c_etaria=c_etaria,
        nota=nota
    )
    db.session.add(nova_serie)
    db.session.commit()

    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    arquivo.save(f'{upload_path}/capa{nova_serie.id}-{timestamp}.jpg')

    return redirect(url_for('lista'))


@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar', id=id)))
    serie = Series.query.filter_by(id=id).first()
    form = FormularioSerie()
    form.nome.data = serie.nome
    form.categoria.data = serie.categoria
    capa_serie = recupera_imagem(id)
    return render_template('editar.html', titulo='Editando Serie', id=id, capa_serie=capa_serie, form=form)


@app.route('/atualizar', methods=['POST', ])
def atualizar():
    form = FormularioSerie(request.form)

    if form.validate_on_submit():
        serie = Series.query.filter_by(id=request.form['id']).first()
        serie.nome = form.nome.data
        serie.categoria = form.categoria.data
        serie.plataforma = form.plataforma.data
        serie.resumo = form.resumo.data
        serie.c_etaria = form.c_etaria.data
        serie.nota = form.nota.data

        db.session.add(serie)
        db.session.commit()

        arquivo = request.files['arquivo']
        upload_path = app.config['UPLOAD_PATH']
        timestamp = time.time()
        deleta_arquivo(id)
        arquivo.save(f'{upload_path}/capa{serie.id}-{timestamp}.jpg')

    return redirect(url_for('lista'))


@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))

    Series.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Serie deletada com sucesso!')

    return redirect(url_for('lista'))


@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)
