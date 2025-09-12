
from app import app
from flask import render_template, url_for, request, redirect
from app.forms import UserForm, LoginForm, LivroForm
from flask_login import login_user, logout_user, current_user, login_required
from app.models import Livro
from sqlalchemy import or_

# Tela inicial
@app.route("/", methods=['GET', 'POST'])
def homepage ():
    return render_template("index.html")

# Página de Login
@app.route ('/login', methods=['GET', 'POST'])
def LoginPage ():
    form = LoginForm()
    if form.validate_on_submit():
        user = form.login ()
        login_user(user, remember=True)
        return redirect(url_for('homepage'))
    return render_template ("usuario_login.html", form=form)

# Página de Cadastro
@app.route ('/cadastro', methods=['GET', 'POST'])
def RegisterPage ():
    form = UserForm ()
    if form.validate_on_submit():
        user = form.save()
        login_user(user, remember=True)
        return redirect(url_for('homepage'))
    return render_template ("usuario_cadastro.html", form=form)

# Deslogar
@app.route('/sair/')
@login_required
def logout ():
    logout_user()
    return redirect(url_for('homepage'))

# Página Livros
@app.route('/livros', methods=['GET', 'POST'])
@login_required
def livros():
    pesquisa = request.args.get('pesquisa', '')
    dados = Livro.query.order_by(Livro.titulo)
    if pesquisa:
        dados = dados.filter(Livro.titulo.ilike(f"%{pesquisa}%"))
    context = {'dados': dados.all()}
    return render_template("livros_lista.html", context=context)

# Página Livros Cadastro
@app.route('/livros/cadastro', methods=['GET', 'POST'])
def livros_cadastro():
    form = LivroForm ()
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('livros'))
    return render_template("livros_cadastro.html", form=form)