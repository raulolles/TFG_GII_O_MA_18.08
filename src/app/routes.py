from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, CambioPuntuacionForm
from app.models import User
from app.filtros.selectOfertas import select_predicciones, select_favoritos, select_aleatorio, select_mejor_valorados, select_mas_jugados, actualizaSelec
from app.filtros.actualizaFiltros import actualiza_filtros, actualiza_yr
import numpy as np

selec = list()

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
@login_required
# Si el usuario está logeado selecciona ofertas
def index():
	global selec
	id_user = current_user.id - 1
	select_modelos, select_users, select_juegos = select_predicciones(id_user)
	selecciones = [{'filtro': 'Modelos', 'select':select_modelos}, {'filtro': 'Usuarios', 'select':select_users}, {'filtro': 'Productos', 'select':select_juegos}]
	selec = selecciones
	texto = '... pensamos que te gustará'
	return redirect(url_for('index2'))

@app.route('/index2', methods=['GET', 'POST'])
@login_required
# Si el usuario está logeado selecciona ofertas
def index2():
	global selec
	if request.args.get('juego') != None:
		juego = int(request.args.get('juego'))
		user = int(request.args.get('user'))
		valor = int(request.args.get('valor'))
		print('-------------------------', juego, user, valor)
		actualiza_yr(juego, user, valor)
		selec = actualizaSelec(juego, valor, selec)
	texto = '... pensamos que te gustará'
	return render_template('index.html', title='Home', selecciones=selec, texto_cab=texto)


@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	select_aleat = select_aleatorio()
	selecciones =[{'filtro':'', 'select':select_aleat}]
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
	return render_template('login.html', title='Sign In', form=form, selecciones=selecciones)

	
@app.route('/favoritos', methods=['GET', 'POST'])
@login_required
# Si el usuario está logeado selecciona ofertas
def favoritos():
		global selec
		id_user = current_user.id - 1
		select_fav = select_favoritos(id_user)
		selecciones =[{'filtro':'Favoritos', 'select':select_fav}]
		selec = selecciones
		texto='... tus juegos favoritos'
		return redirect(url_for('favoritos2'))

		
@app.route('/favoritos2', methods=['GET', 'POST'])
@login_required
# Si el usuario está logeado selecciona ofertas
def favoritos2():
	global selec
	if request.args.get('juego') != None:
		juego = int(request.args.get('juego'))
		user = int(request.args.get('user'))
		valor = int(request.args.get('valor'))
		actualiza_yr(juego, user, valor)
		selec = actualizaSelec(juego, valor, selec)
	texto='... tus juegos favoritos'
	return render_template('index.html', title='Favoritos', selecciones=selec, texto_cab=texto)


@app.route('/mas_jugados', methods=['GET', 'POST'])
@login_required
def mas_jugados():
	global selec
	id_user = current_user.id - 1
	select_mas_jug = select_mas_jugados(id_user)
	selecciones =[{'filtro':'Más Jugados', 'select':select_mas_jug}]
	selec = selecciones
	texto='... los más jugados por todos los usuarios'
	return redirect(url_for('mas_jugados2'))
	
	
@app.route('/mas_jugados2', methods=['GET', 'POST'])
@login_required
def mas_jugados2():
	global selec
	if request.args.get('juego') != None:
		juego = int(request.args.get('juego'))
		user = int(request.args.get('user'))
		valor = int(request.args.get('valor'))
		actualiza_yr(juego, user, valor)
		selec = actualizaSelec(juego, valor, selec)
	texto='... los más jugados por todos los usuarios'
	return render_template('index.html', title='Mas Jugados', selecciones=selec, texto_cab=texto)
	

@app.route('/mejor_valorados', methods=['GET', 'POST'])
@login_required
def mejor_valorados():
	global selec
	id_user = current_user.id - 1
	select_valor = select_mejor_valorados(id_user)
	selecciones =[{'filtro':'Mejor Valorados', 'select':select_valor}]
	selec = selecciones
	texto='... los mejor valorados por todos los usuarios'
	return redirect(url_for('mejor_valorados2'))
	

@app.route('/mejor_valorados2', methods=['GET', 'POST'])
@login_required
def mejor_valorados2():
	global selec
	if request.args.get('juego') != None:
		juego = int(request.args.get('juego'))
		user = int(request.args.get('user'))
		valor = int(request.args.get('valor'))
		actualiza_yr(juego, user, valor)
		selec = actualizaSelec(juego, valor, selec)
	texto='... los mejor valorados por todos los usuarios'
	return render_template('index.html', title='Mejor Valorados', selecciones=selec, texto_cab=texto)
	
	
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(username=form.username.data, email=form.email.data, avatar='img'+str(np.random.randint(1,31)))
		user.set_password(form.password.data)
		
		# Actuliza las tablas e Insercción en BD
		actualiza_filtros()
		db.session.add(user)
		db.session.commit()
		
		flash('Congratulations, you are now a registered user!')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)
