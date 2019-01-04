from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User
from app.filtros.selectOfertas import select
from app.filtros.actualizaFiltros import actualizaFiltros
import numpy as np

@app.route('/')
@app.route('/index')
@login_required
# Si el usuario está logeado selecciona ofertas
def index():
	idUser = current_user.id - 1
	selectModelos, selectUsers, selectJuegos = select(idUser)
	selecciones = [{'filtro': 'Modelos', 'select':selectModelos}, {'filtro': 'Usuarios', 'select':selectUsers}, {'filtro': 'Productos', 'select':selectJuegos}]
	return render_template('index.html', title='Home', selecciones=selecciones)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
	return render_template('index.html', title='Register', form=form)
