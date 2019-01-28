from flask import render_template, flash, redirect, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, SearchForm
from app.models import User
from app.filtros.selectOfertas import select_predicciones, select_favoritos, select_aleatorio, select_mejor_valorados, select_mas_jugados, actualizaSelec, select_busqueda, select_archive
from app.filtros.actualizaFiltros import actualiza_filtros, actualiza_yr
from datetime import datetime
import copy
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
	jg_ifrm = None
	if request.args.get('juego') != None:
		juego = int(request.args.get('juego'))
		user = int(request.args.get('user'))
		valor = int(request.args.get('valor'))
		actualiza_yr(juego, user, valor)
		if request.args.get('jg_ifrm') != "":
			jg_ifrm = int(request.args.get('jg_ifrm'))
			
		selec = actualizaSelec(juego, valor, selec)
	texto = '... pensamos que te gustará'
	return render_template('index.html', title='Home', selecciones=selec, texto_cab=texto, jg_ifrm=jg_ifrm)


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
	jg_ifrm = None
	if request.args.get('juego') != None:
		juego = int(request.args.get('juego'))
		user = int(request.args.get('user'))
		valor = int(request.args.get('valor'))
		actualiza_yr(juego, user, valor)
		if request.args.get('jg_ifrm') != "":
			jg_ifrm = int(request.args.get('jg_ifrm'))

		selec = actualizaSelec(juego, valor, selec)
	texto='... tus juegos favoritos'
	
	page = request.args.get('page', 1, type=int)
	next_url, prev_url, inic_url, fin_url, total_pag, selecciones = calc_paginacion(page, selec, 'favoritos2')
	return render_template('index.html', title='Favoritos', selecciones=selecciones, texto_cab=texto, next_url=next_url, prev_url=prev_url, inic_url=inic_url, fin_url=fin_url, pag=page, total_pag=total_pag, jg_ifrm=jg_ifrm)


@app.route('/mas_jugados_todos', methods=['GET', 'POST'])
@login_required
def mas_jugados_todos():
	global selec
	id_user = current_user.id - 1
	select_mas_jug = select_mas_jugados(id_user,3)
	selecciones =[{'filtro':'Más Jugados: Todos los juegos', 'select':select_mas_jug}]
	selec = selecciones
	texto='... los más jugados por todos los usuarios'
	return redirect(url_for('mas_jugados2_todos'))
	
	
@app.route('/mas_jugados2_todos', methods=['GET', 'POST'])
@login_required
def mas_jugados2_todos():
	global selec
	jg_ifrm = None
	if request.args.get('juego') != None:
		juego = int(request.args.get('juego'))
		user = int(request.args.get('user'))
		valor = int(request.args.get('valor'))
		actualiza_yr(juego, user, valor)
		if request.args.get('jg_ifrm') != "":
			jg_ifrm = int(request.args.get('jg_ifrm'))
			
		selec = actualizaSelec(juego, valor, selec)
	texto='... los más jugados por todos los usuarios'
	
	page = request.args.get('page', 1, type=int)
	next_url, prev_url, inic_url, fin_url, total_pag, selecciones = calc_paginacion(page, selec, 'mas_jugados2_todos')
	return render_template('index.html', title='Mas Jugados', selecciones=selecciones, texto_cab=texto, next_url=next_url, prev_url=prev_url, inic_url=inic_url, fin_url=fin_url, pag=page, total_pag=total_pag, jg_ifrm=jg_ifrm)
	


@app.route('/mas_jugados_ya_jugado', methods=['GET', 'POST'])
@login_required
def mas_jugados_ya_jugado():
	global selec
	id_user = current_user.id - 1
	select_mas_jug = select_mas_jugados(id_user,1)
	selecciones =[{'filtro':'Más Jugados: Jugados antes por ti', 'select':select_mas_jug}]
	selec = selecciones
	texto='... los más jugados por todos los usuarios'
	return redirect(url_for('mas_jugados2_ya_jugado'))
	
	
@app.route('/mas_jugados2_ya_jugado', methods=['GET', 'POST'])
@login_required
def mas_jugados2_ya_jugado():
	global selec
	jg_ifrm = None
	if request.args.get('juego') != None:
		juego = int(request.args.get('juego'))
		user = int(request.args.get('user'))
		valor = int(request.args.get('valor'))
		actualiza_yr(juego, user, valor)
		if request.args.get('jg_ifrm') != "":
			jg_ifrm = int(request.args.get('jg_ifrm'))
			
		selec = actualizaSelec(juego, valor, selec)
	texto='... los más jugados por todos los usuarios'
	
	page = request.args.get('page', 1, type=int)
	next_url, prev_url, inic_url, fin_url, total_pag, selecciones = calc_paginacion(page, selec, 'mas_jugados2_ya_jugado')
	return render_template('index.html', title='Mas Jugados', selecciones=selecciones, texto_cab=texto, next_url=next_url, prev_url=prev_url, inic_url=inic_url, fin_url=fin_url, pag=page, total_pag=total_pag, jg_ifrm=jg_ifrm)
		
		
@app.route('/mas_jugados_no_jugado', methods=['GET', 'POST'])
@login_required
def mas_jugados_no_jugado():
	global selec
	id_user = current_user.id - 1
	select_mas_jug = select_mas_jugados(id_user,0)
	selecciones =[{'filtro':'Más Jugados: Aún no has jugado', 'select':select_mas_jug}]
	selec = selecciones
	texto='... los más jugados por todos los usuarios'
	return redirect(url_for('mas_jugados2_no_jugado'))
	
	
@app.route('/mas_jugados2_no_jugado', methods=['GET', 'POST'])
@login_required
def mas_jugados2_no_jugado():
	global selec
	jg_ifrm = None
	if request.args.get('juego') != None:
		juego = int(request.args.get('juego'))
		user = int(request.args.get('user'))
		valor = int(request.args.get('valor'))
		actualiza_yr(juego, user, valor)
		if request.args.get('jg_ifrm') != "":
			jg_ifrm = int(request.args.get('jg_ifrm'))
			
		selec = actualizaSelec(juego, valor, selec)
	texto='... los más jugados por todos los usuarios'
	
	page = request.args.get('page', 1, type=int)
	next_url, prev_url, inic_url, fin_url, total_pag, selecciones = calc_paginacion(page, selec, 'mas_jugados2_no_jugado')
	return render_template('index.html', title='Mas Jugados', selecciones=selecciones, texto_cab=texto, next_url=next_url, prev_url=prev_url, inic_url=inic_url, fin_url=fin_url, pag=page, total_pag=total_pag, jg_ifrm=jg_ifrm)
		

		
@app.route('/mejor_valorados_todos', methods=['GET', 'POST'])
@login_required
def mejor_valorados_todos():
	global selec
	id_user = current_user.id - 1
	select_valor = select_mejor_valorados(id_user, 3)
	selecciones =[{'filtro':'Mejor Valorados: Todos los Juegos', 'select':select_valor}]
	selec = selecciones
	texto='... los mejor valorados por todos los usuarios'
	return redirect(url_for('mejor_valorados2_todos'))
	

@app.route('/mejor_valorados2_todos', methods=['GET', 'POST'])
@login_required
def mejor_valorados2_todos():
	global selec
	jg_ifrm = None
	if request.args.get('juego') != None:
		juego = int(request.args.get('juego'))
		user = int(request.args.get('user'))
		valor = int(request.args.get('valor'))
		actualiza_yr(juego, user, valor)
		if request.args.get('jg_ifrm') != "":
			jg_ifrm = int(request.args.get('jg_ifrm'))
			
		selec = actualizaSelec(juego, valor, selec)
	texto='... los mejor valorados por todos los usuarios'
	
	page = request.args.get('page', 1, type=int)
	next_url, prev_url, inic_url, fin_url, total_pag, selecciones = calc_paginacion(page, selec,'mejor_valorados2_todos')
	return render_template('index.html', title='Mejor Valorados', selecciones=selecciones, texto_cab=texto, next_url=next_url, prev_url=prev_url, inic_url=inic_url, fin_url=fin_url, pag = page, total_pag = total_pag, jg_ifrm=jg_ifrm)

			
@app.route('/mejor_valorados_ya_jugado', methods=['GET', 'POST'])
@login_required
def mejor_valorados_ya_jugado():
	global selec
	id_user = current_user.id - 1
	select_valor = select_mejor_valorados(id_user, 1)
	selecciones =[{'filtro':'Mejor Valorados: Jugados antes por ti', 'select':select_valor}]
	selec = selecciones
	texto='... los mejor valorados por todos los usuarios'
	return redirect(url_for('mejor_valorados2_ya_jugados'))
	

@app.route('/mejor_valorados2_ya_jugados', methods=['GET', 'POST'])
@login_required
def mejor_valorados2_ya_jugados():
	global selec
	jg_ifrm = None
	if request.args.get('juego') != None:
		juego = int(request.args.get('juego'))
		user = int(request.args.get('user'))
		valor = int(request.args.get('valor'))
		actualiza_yr(juego, user, valor)
		if request.args.get('jg_ifrm') != "":
			jg_ifrm = int(request.args.get('jg_ifrm'))
			
		selec = actualizaSelec(juego, valor, selec)
	texto='... los mejor valorados por todos los usuarios'
	
	page = request.args.get('page', 1, type=int)
	next_url, prev_url, inic_url, fin_url, total_pag, selecciones = calc_paginacion(page, selec,'mejor_valorados2_ya_jugados')
	return render_template('index.html', title='Mejor Valorados', selecciones=selecciones, texto_cab=texto, next_url=next_url, prev_url=prev_url, inic_url=inic_url, fin_url=fin_url, pag = page, total_pag = total_pag, jg_ifrm=jg_ifrm)
		
		
@app.route('/mejor_valorados_no_jugado', methods=['GET', 'POST'])
@login_required
def mejor_valorados_no_jugado():
	global selec
	id_user = current_user.id - 1
	select_valor = select_mejor_valorados(id_user, 0)
	selecciones =[{'filtro':'Mejor Valorados: Aún no has jugado', 'select':select_valor}]
	selec = selecciones
	texto='... los mejor valorados por todos los usuarios'
	return redirect(url_for('mejor_valorados2_no_jugado'))
	

@app.route('/mejor_valorados2_no_jugado', methods=['GET', 'POST'])
@login_required
def mejor_valorados2_no_jugado():
	global selec
	jg_ifrm = None
	if request.args.get('juego') != None:
		juego = int(request.args.get('juego'))
		user = int(request.args.get('user'))
		valor = int(request.args.get('valor'))
		actualiza_yr(juego, user, valor)
		if request.args.get('jg_ifrm') != "":
			jg_ifrm = int(request.args.get('jg_ifrm'))
			
		selec = actualizaSelec(juego, valor, selec)
	texto='... los mejor valorados por todos los usuarios'
	
	page = request.args.get('page', 1, type=int)
	next_url, prev_url, inic_url, fin_url, total_pag, selecciones = calc_paginacion(page, selec,'mejor_valorados2_no_jugado')
	return render_template('index.html', title='Mejor Valorados', selecciones=selecciones, texto_cab=texto, next_url=next_url, prev_url=prev_url, inic_url=inic_url, fin_url=fin_url, pag = page, total_pag = total_pag, jg_ifrm=jg_ifrm)

	

@app.route('/mas_vistos_archive_todos', methods=['GET', 'POST'])
@login_required
def mas_vistos_archive_todos():
	global selec
	id_user = current_user.id - 1
	select_valor = select_archive(id_user, 'visitas', 3)
	selecciones =[{'filtro':'Mas vistos en archive.org: Todos los Juegos', 'select':select_valor}]
	selec = selecciones
	texto='... los más vistos en archive.org'
	return redirect(url_for('mas_vistos_archive2_todos'))
	

@app.route('/mas_vistos_archive2_todos', methods=['GET', 'POST'])
@login_required
def mas_vistos_archive2_todos():
	global selec
	jg_ifrm = None
	if request.args.get('juego') != None:
		juego = int(request.args.get('juego'))
		user = int(request.args.get('user'))
		valor = int(request.args.get('valor'))
		actualiza_yr(juego, user, valor)
		if request.args.get('jg_ifrm') != "":
			jg_ifrm = int(request.args.get('jg_ifrm'))
			
		selec = actualizaSelec(juego, valor, selec)
	texto='... los más vistos en archive.org'
	
	page = request.args.get('page', 1, type=int)
	next_url, prev_url, inic_url, fin_url, total_pag, selecciones = calc_paginacion(page, selec,'mas_vistos_archive2_todos')
	return render_template('index.html', title='Mas Vistos', selecciones=selecciones, texto_cab=texto, next_url=next_url, prev_url=prev_url, inic_url=inic_url, fin_url=fin_url, pag = page, total_pag = total_pag, jg_ifrm=jg_ifrm)

	
@app.route('/mas_vistos_archive_ya_jugado', methods=['GET', 'POST'])
@login_required
def mas_vistos_archive_ya_jugado():
	global selec
	id_user = current_user.id - 1
	select_valor = select_archive(id_user, 'visitas', 1)
	selecciones =[{'filtro':'Mas vistos en archive.org: Jugados antes por ti', 'select':select_valor}]
	selec = selecciones
	texto='... los más vistos en archive.org'
	return redirect(url_for('mas_vistos_archive2_ya_jugado'))
	

@app.route('/mas_vistos_archive2_ya_jugado', methods=['GET', 'POST'])
@login_required
def mas_vistos_archive2_ya_jugado():
	global selec
	jg_ifrm = None
	if request.args.get('juego') != None:
		juego = int(request.args.get('juego'))
		user = int(request.args.get('user'))
		valor = int(request.args.get('valor'))
		actualiza_yr(juego, user, valor)
		if request.args.get('jg_ifrm') != "":
			jg_ifrm = int(request.args.get('jg_ifrm'))
			
		selec = actualizaSelec(juego, valor, selec)
	texto='... los más vistos en archive.org'
	
	page = request.args.get('page', 1, type=int)
	next_url, prev_url, inic_url, fin_url, total_pag, selecciones = calc_paginacion(page, selec,'mas_vistos_archive2_ya_jugado')
	return render_template('index.html', title='Mas Vistos', selecciones=selecciones, texto_cab=texto, next_url=next_url, prev_url=prev_url, inic_url=inic_url, fin_url=fin_url, pag = page, total_pag = total_pag, jg_ifrm=jg_ifrm)


	
@app.route('/mas_vistos_archive_no_jugado', methods=['GET', 'POST'])
@login_required
def mas_vistos_archive_no_jugado():
	global selec
	id_user = current_user.id - 1
	select_valor = select_archive(id_user, 'visitas', 0)
	selecciones =[{'filtro':'Mas vistos en archive.org: Aún no has jugado', 'select':select_valor}]
	selec = selecciones
	texto='... los más vistos en archive.org'
	return redirect(url_for('mas_vistos_archive2_no_jugado'))
	

@app.route('/mas_vistos_archive2_no_jugado', methods=['GET', 'POST'])
@login_required
def mas_vistos_archive2_no_jugado():
	global selec
	jg_ifrm = None
	if request.args.get('juego') != None:
		juego = int(request.args.get('juego'))
		user = int(request.args.get('user'))
		valor = int(request.args.get('valor'))
		actualiza_yr(juego, user, valor)
		if request.args.get('jg_ifrm') != "":
			jg_ifrm = int(request.args.get('jg_ifrm'))
			
		selec = actualizaSelec(juego, valor, selec)
	texto='... los más vistos en archive.org'
	
	page = request.args.get('page', 1, type=int)
	next_url, prev_url, inic_url, fin_url, total_pag, selecciones = calc_paginacion(page, selec,'mas_vistos_archive2_no_jugado')
	return render_template('index.html', title='Mas Vistos', selecciones=selecciones, texto_cab=texto, next_url=next_url, prev_url=prev_url, inic_url=inic_url, fin_url=fin_url, pag = page, total_pag = total_pag, jg_ifrm=jg_ifrm)
	
	
	
@app.route('/mas_stars_archive', methods=['GET', 'POST'])
@login_required
def mas_stars_archive_todos():
	global selec
	id_user = current_user.id - 1
	select_valor = select_archive(id_user, 'favoritos', 3)
	selecciones =[{'filtro':'Mas stars en archive.org: Todos los Juegos', 'select':select_valor}]
	selec = selecciones
	texto='... con más stars en archive.org'
	return redirect(url_for('mas_stars_archive2_todos'))
	

@app.route('/mas_stars_archive2_todos', methods=['GET', 'POST'])
@login_required
def mas_stars_archive2_todos():
	global selec
	jg_ifrm = None
	if request.args.get('juego') != None:
		juego = int(request.args.get('juego'))
		user = int(request.args.get('user'))
		valor = int(request.args.get('valor'))
		actualiza_yr(juego, user, valor)
		if request.args.get('jg_ifrm') != "":
			jg_ifrm = int(request.args.get('jg_ifrm'))
			
		selec = actualizaSelec(juego, valor, selec)
	texto='... con más stars en archive.org'
	
	page = request.args.get('page', 1, type=int)
	next_url, prev_url, inic_url, fin_url, total_pag, selecciones = calc_paginacion(page, selec,'mas_stars_archive2_todos')
	return render_template('index.html', title='Mas Stars', selecciones=selecciones, texto_cab=texto, next_url=next_url, prev_url=prev_url, inic_url=inic_url, fin_url=fin_url, pag = page, total_pag = total_pag, jg_ifrm=jg_ifrm)

	
	
@app.route('/mas_stars_archive_ya_jugado', methods=['GET', 'POST'])
@login_required
def mas_stars_archive_ya_jugado():
	global selec
	id_user = current_user.id - 1
	select_valor = select_archive(id_user, 'favoritos', 1)
	selecciones =[{'filtro':'Mas stars en archive.org', 'select':select_valor}]
	selec = selecciones
	texto='... con más stars en archive.org'
	return redirect(url_for('mas_stars_archive2_ya_jugado'))
	

@app.route('/mas_stars_archive2_ya_jugado', methods=['GET', 'POST'])
@login_required
def mas_stars_archive2_ya_jugado():
	global selec
	jg_ifrm = None
	if request.args.get('juego') != None:
		juego = int(request.args.get('juego'))
		user = int(request.args.get('user'))
		valor = int(request.args.get('valor'))
		actualiza_yr(juego, user, valor)
		if request.args.get('jg_ifrm') != "":
			jg_ifrm = int(request.args.get('jg_ifrm'))
			
		selec = actualizaSelec(juego, valor, selec)
	texto='... con más stars en archive.org'
	
	page = request.args.get('page', 1, type=int)
	next_url, prev_url, inic_url, fin_url, total_pag, selecciones = calc_paginacion(page, selec,'mas_stars_archive2_ya_jugado')
	return render_template('index.html', title='Mas Stars', selecciones=selecciones, texto_cab=texto, next_url=next_url, prev_url=prev_url, inic_url=inic_url, fin_url=fin_url, pag = page, total_pag = total_pag, jg_ifrm=jg_ifrm)

	
	
@app.route('/mas_stars_archive_no_jugado', methods=['GET', 'POST'])
@login_required
def mas_stars_archive_no_jugado():
	global selec
	id_user = current_user.id - 1
	select_valor = select_archive(id_user, 'favoritos', 0)
	selecciones =[{'filtro':'Mas stars en archive.org: Aún no has jugado', 'select':select_valor}]
	selec = selecciones
	texto='... con más stars en archive.org'
	return redirect(url_for('mas_stars_archive2_no_jugado'))
	

@app.route('/mas_stars_archive2_no_jugado', methods=['GET', 'POST'])
@login_required
def mas_stars_archive2_no_jugado():
	global selec
	jg_ifrm = None
	if request.args.get('juego') != None:
		juego = int(request.args.get('juego'))
		user = int(request.args.get('user'))
		valor = int(request.args.get('valor'))
		actualiza_yr(juego, user, valor)
		if request.args.get('jg_ifrm') != "":
			jg_ifrm = int(request.args.get('jg_ifrm'))
			
		selec = actualizaSelec(juego, valor, selec)
	texto='... con más stars en archive.org'
	
	page = request.args.get('page', 1, type=int)
	next_url, prev_url, inic_url, fin_url, total_pag, selecciones = calc_paginacion(page, selec,'mas_stars_archive2_no_jugado')
	return render_template('index.html', title='Mas Stars', selecciones=selecciones, texto_cab=texto, next_url=next_url, prev_url=prev_url, inic_url=inic_url, fin_url=fin_url, pag = page, total_pag = total_pag, jg_ifrm=jg_ifrm)


@app.route('/mas_comments_archive_todos', methods=['GET', 'POST'])
@login_required
def mas_comments_archive_todos():
	global selec
	id_user = current_user.id - 1
	select_valor = select_archive(id_user, 'comentarios', 3)
	selecciones =[{'filtro':'con más comentarios en archive.org: Todos los Juegos', 'select':select_valor}]
	selec = selecciones
	texto='... con más comentarios en archive.org'
	return redirect(url_for('mas_comments_archive2_todos'))
	

@app.route('/mas_comments_archive2_todos', methods=['GET', 'POST'])
@login_required
def mas_comments_archive2_todos():
	global selec
	jg_ifrm = None
	if request.args.get('juego') != None:
		juego = int(request.args.get('juego'))
		user = int(request.args.get('user'))
		valor = int(request.args.get('valor'))
		actualiza_yr(juego, user, valor)
		if request.args.get('jg_ifrm') != "":
			jg_ifrm = int(request.args.get('jg_ifrm'))
			
		selec = actualizaSelec(juego, valor, selec)
	texto='... con más comentarios en archive.org'
	
	page = request.args.get('page', 1, type=int)
	next_url, prev_url, inic_url, fin_url, total_pag, selecciones = calc_paginacion(page, selec,'mas_comments_archive2_todos')
	return render_template('index.html', title='Mas Comments', selecciones=selecciones, texto_cab=texto, next_url=next_url, prev_url=prev_url, inic_url=inic_url, fin_url=fin_url, pag = page, total_pag = total_pag, jg_ifrm=jg_ifrm)


@app.route('/mas_comments_archive_ya_jugado', methods=['GET', 'POST'])
@login_required
def mas_comments_archive_ya_jugado():
	global selec
	id_user = current_user.id - 1
	select_valor = select_archive(id_user, 'comentarios', 1)
	selecciones =[{'filtro':'con más comentarios en archive.org: Jugados antes por ti', 'select':select_valor}]
	selec = selecciones
	texto='... con más comentarios en archive.org'
	return redirect(url_for('mas_comments_archive2_ya_jugado'))
	

@app.route('/mas_comments_archive2_ya_jugado', methods=['GET', 'POST'])
@login_required
def mas_comments_archive2_ya_jugado():
	global selec
	jg_ifrm = None
	if request.args.get('juego') != None:
		juego = int(request.args.get('juego'))
		user = int(request.args.get('user'))
		valor = int(request.args.get('valor'))
		actualiza_yr(juego, user, valor)
		if request.args.get('jg_ifrm') != "":
			jg_ifrm = int(request.args.get('jg_ifrm'))
			
		selec = actualizaSelec(juego, valor, selec)
	texto='... con más comentarios en archive.org'
	
	page = request.args.get('page', 1, type=int)
	next_url, prev_url, inic_url, fin_url, total_pag, selecciones = calc_paginacion(page, selec,'mas_comments_archive2_ya_jugado')
	return render_template('index.html', title='Mas Comments', selecciones=selecciones, texto_cab=texto, next_url=next_url, prev_url=prev_url, inic_url=inic_url, fin_url=fin_url, pag = page, total_pag = total_pag, jg_ifrm=jg_ifrm)

	

@app.route('/mas_comments_archive_no_jugado', methods=['GET', 'POST'])
@login_required
def mas_comments_archive_no_jugado():
	global selec
	id_user = current_user.id - 1
	select_valor = select_archive(id_user, 'comentarios', 0)
	selecciones =[{'filtro':'con más comentarios en archive.org: Aún no has jugado', 'select':select_valor}]
	selec = selecciones
	texto='... con más comentarios en archive.org'
	return redirect(url_for('mas_comments_archive2_no_jugado'))
	

@app.route('/mas_comments_archive2_no_jugado', methods=['GET', 'POST'])
@login_required
def mas_comments_archive2_no_jugado():
	global selec
	jg_ifrm = None
	if request.args.get('juego') != None:
		juego = int(request.args.get('juego'))
		user = int(request.args.get('user'))
		valor = int(request.args.get('valor'))
		actualiza_yr(juego, user, valor)
		if request.args.get('jg_ifrm') != "":
			jg_ifrm = int(request.args.get('jg_ifrm'))
			
		selec = actualizaSelec(juego, valor, selec)
	texto='... con más comentarios en archive.org'
	
	page = request.args.get('page', 1, type=int)
	next_url, prev_url, inic_url, fin_url, total_pag, selecciones = calc_paginacion(page, selec,'mas_comments_archive2_no_jugado')
	return render_template('index.html', title='Mas Comments', selecciones=selecciones, texto_cab=texto, next_url=next_url, prev_url=prev_url, inic_url=inic_url, fin_url=fin_url, pag = page, total_pag = total_pag, jg_ifrm=jg_ifrm)


	
@app.route('/busqueda', methods=['GET', 'POST'])
@login_required
def busqueda():
	global selec
	id_user = current_user.id - 1
	palabra_busq = request.args.get('q')
	text_filtro = 'Busqueda: ' + palabra_busq
	select_busq = select_busqueda(id_user, palabra_busq)
	selecciones =[{'filtro': text_filtro, 'select':select_busq}]
	selec = selecciones
	texto='... los resultados de tu búsqueda'
	return redirect(url_for('busqueda2'))
	

@app.route('/busqueda2', methods=['GET', 'POST'])
@login_required
def busqueda2():
	global selec
	jg_ifrm = None
	if request.args.get('juego') != None:
		juego = int(request.args.get('juego'))
		user = int(request.args.get('user'))
		valor = int(request.args.get('valor'))
		actualiza_yr(juego, user, valor)
		if request.args.get('jg_ifrm') != "":
			jg_ifrm = int(request.args.get('jg_ifrm'))

		selec = actualizaSelec(juego, valor, selec)
	texto= ' ... los resultados de tu búsqueda'
	page = request.args.get('page', 1, type=int)
	next_url, prev_url, inic_url, fin_url, total_pag, selecciones = calc_paginacion(page, selec,'busqueda2')
	
	return render_template('index.html', title='Busqueda', selecciones=selecciones, texto_cab=texto, next_url=next_url, prev_url=prev_url, inic_url=inic_url, fin_url=fin_url, pag=page, total_pag=total_pag, jg_ifrm=jg_ifrm)
	
	
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
		avatar = form.avatar.data
		
		if avatar is None:
			avatar = 'img12'
		else:
			avatar = 'img'+str(avatar)

		user = User(username=form.username.data, email=form.email.data, avatar=avatar)
		user.set_password(form.password.data)
		
		# Actuliza las tablas e Insercción en BD
		actualiza_filtros()
		db.session.add(user)
		db.session.commit()
		
		flash('Felicidades, ya eres un usuario registrado!')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)


	
def calc_paginacion(page, selec, origen):
	inc_selec = (page-1)*app.config['SEL_POR_PAG']
	fin_selec = page*app.config['SEL_POR_PAG']
	selecciones = copy.deepcopy(selec)
	selecciones[0]['select'] = selec[0]['select'][inc_selec: fin_selec]
	
	if len(selec[0]['select']) % app.config['SEL_POR_PAG'] == 0:
		total_pag = len(selec[0]['select']) // app.config['SEL_POR_PAG']
	else:
		total_pag = len(selec[0]['select']) // app.config['SEL_POR_PAG'] + 1
		
	if page > 1:
		pag_ante = page - 1
	else:
		pag_ante = page
		
	if page < total_pag:
		pag_post = page+1
	else:
		pag_post = page
		
	next_url = url_for(origen, page=pag_post)
	prev_url = url_for(origen, page=pag_ante)
	inic_url = url_for(origen, page=1)
	fin_url = url_for(origen, page=total_pag)
	
	return next_url, prev_url, inic_url, fin_url, total_pag, selecciones