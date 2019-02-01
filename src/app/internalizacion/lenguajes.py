# -*- coding: utf-8 -*-
"""
Crea y suministra los diccionarios con las palabras a incluir en la web
para los diferentes lenguajes
"""

def crea_dicc_lenguajes():

	diccionario_todos_lenguajes = {'es' : 
			{'sesion_leng':'es',
			
			'menu_inicio':'Inicio',
			'menu_favoritos':'Favoritos',
			'menu_en_retrogaming':'en Retrogaming',
			'menu_en_archive':'en Archive.org',
			'menu_todos_juegos':'Todos los Juegos',
			'menu_ya_jugados':'Ya has jugado',
			'menu_no_has_jugado':'No has jugado',
			'menu_mas_vistos':'Mas Vistos',
			'menu_mas_stars':'Mas Stars',
			'menu_mas_comments':'Mas Comments',
			'menu_mas_jugados':'Mas Jugados',
			'menu_mejor_valorados':'Mejor Valorados',
			'menu_busqueda':'Búsqueda',
			'menu_login':'Inicio Sesión',
			'menu_logout':'Salir',
			
			'saludo':'Hola!',
			
			'pg_login_iniciar_sesion':'Iniciar Sesion',
			'pg_login_usuario':'Nombre Usuario',
			'pg_login_contras':'Contraseña',
			'pg_login_recordarme':'Recordarme',
			'pg_login_iniciar':'Iniciar Sesión',
			'pg_login_nuevo_user':'Nuevo Usuario?',
			'pg_login_click_reg':'Click para Registrarse!',
			'pg_login_error1':'[ Valor Requerido ]',
			'pg_login_men_error_base':'Por favor, identifíquese para acceder a esta página.',
			'pg_login_error_ident':'Nombre de usuario o contraseña erronea',
			
			'pg_reg_registro':'Registro',
			'pg_reg_usuario':'Usuario',
			'pg_reg_email':'Email',
			'pg_reg_contrasena':'Contraseña',
			'pg_reg_repe_contr':'Repetir Contraseña',
			'pg_reg_registrar':'Registrar',
			'pg_reg_registro_ok':'Felicidades, ya eres un usuario registrado!',
			'pg_reg_error_user':'[ Use un nombre de usuario diferente]',
			'pg_reg_error_email':'[ Email no valido ]',
			'pg_reg_error_contrasena':'[ Contraseña no valida ]',
			'pg_reg_error_contrasena_rep':'[ El valor debe coincidir con la contraseña ] ',

			'pg_ind_text':'...pensamos que te gustará',
			'pg_ind_tit_selec_modelos':'Modelos',
			'pg_ind_tit_selec_usuarios':'Usuarios',
			'pg_ind_tit_selec_productos':'Productos',
			
			'pg_ind_text_favoritos':'...tus juegos favoritos',			
			'pg_ind_tit_selec_favoritos':'Favoritos',
			
			'pg_ind_text_mas_jugados_todos':'...los más jugados por todos los usuarios',
			'pg_ind_text_mejor_valor_todos':'...los mejor valorados por todos los usuarios',
			
			
			'pg_ind_tit_selec_mas_jugados':'Más Jugados',
			'pg_ind_tit_selec_mejor_valorados':'Mejor Valorados',

			'pg_ind_tit_selec_todos_juegos':' : Todos los juegos',
			'pg_ind_tit_selec_ya_jugados':' : Jugados antes por ti',
			'pg_ind_tit_selec_no_jugados':' : Aún no has jugado',
			
			'pg_ind_text_mas_vistos_archive':'...los más vistos en archive.org',
			'pg_ind_text_mas_stars_archive':'...con más stars en archive.org',
			'pg_ind_text_mas_comments_archive':'...con más comentarios en archive.org',
			
			'pg_ind_tit_selec_mas_vistos':'Más Vistos en archive.org',
			'pg_ind_tit_selec_mas_stars':'Con más stars en archive.org',
			'pg_ind_tit_selec_mas_comments':'Con más comentarios en archive.org',
			
			'pg_ind_text_busqueda':'...los resultados de tu búsqueda',
			'pg_ind_tit_selec_busqueda':'Busqueda',
			
			'tira_juego_juega':'juega en su web',
			'tira_juego_tu_valoracion':'tu valoración',
			
			'iframe_cerrar':'Cerrar Juego',
			
			'paginacion_pagina':'página',
			'paginacion_de':'de',
			'paginacion_inicio':'inicio',
			'paginacion_final':'final',
			'paginacion_anterior':'anterior',
			'paginacion_siguient':'siguiente',

			'introd_1':'Retrogaming Recommender',
			'introd_2':'Commodore 64',
			'introd_3':'Podrás ver más de 10.000 juegos de la mítica commodore 64.',
			'introd_4':'Dispondrás de predicciones de los juegos que mejor se adaptan a tu trayectoria de juego.',
			'introd_5':'Puntua cada juego según tu preferencias. Lista y busca juegos según han sido puntuados en Retrogaming o en Archive.org',
			'introd_6':'La lista de juegos está basada en los que se encuetran disponibles en web archive.org'			
			},
		'en' : 
			{'sesion_leng':'en',
			
			'menu_inicio':'Home',
			'menu_favoritos':'FavoIngl',
			'menu_en_retrogaming':'in Retrogaming',
			'menu_en_archive':'in Archive.org',
			'menu_todos_juegos':'Todos los Juegos',
			'menu_ya_jugados':'Ya has jugado',
			'menu_no_has_jugado':'No has jugado',
			'menu_mas_vistos':'Mas Vistos',
			'menu_mas_stars':'Mas Stars',
			'menu_mas_comments':'Mas Comments',
			'menu_mas_jugados':'Mas Jugados',
			'menu_mejor_valorados':'Mejor Valorados',
			'menu_busqueda':'Search',
			'menu_login':'Login',
			'menu_logout':'Logout',
			
			'saludo':'Hi!',
			
			'pg_login_iniciar_sesion':'Iniciar Sesion',
			'pg_login_usuario':'Usurio',
			'pg_login_contras':'Contraseña',
			'pg_login_recordarme':'Recordarme',
			'pg_login_iniciar':'Iniciar Sesión',
			'pg_login_nuevo_user':'Nuevo Usuario?',
			'pg_login_click_reg':'Click para Registrarse!',
			'pg_login_error1':'[ This field is required ]',
			'pg_login_men_error_base':'Please log in to access this page.',
			'pg_login_error_ident':'Invalid username or password',
			
			'pg_reg_registro':'Register',
			'pg_reg_usuario':'Usuario',
			'pg_reg_email':'Email',
			'pg_reg_contrasena':'Contraseña',
			'pg_reg_repe_contr':'Repetir Contraseña',
			'pg_reg_registrar':'Register',
			'pg_reg_registro_ok':'Felicidades, ya eres un usuario registrado!',
			'pg_reg_error_user':'[ Use un nombre de usuario diferente]',
			'pg_reg_error_email':'[ Invalid email address ]',
			'pg_reg_error_contrasena':'[ Contraseña no valida ]',
			'pg_reg_error_contrasena_rep':'[ Field must be equal to password ] ',			
			
			'pg_ind_text':'...pensamos que te gustará Ingles',
			'pg_ind_tit_selec_modelos':'Modelos2',
			'pg_ind_tit_selec_usuarios':'Usuarios2',
			'pg_ind_tit_selec_productos':'Productos2',
			'pg_ind_text_favoritos':'...tus juegos favoritos Ingles',			
			'pg_ind_tit_selec_favoritos':'Favoritos ingles',
			
			'pg_ind_text_mas_jugados_todos':'...los más jugados por todos los usuarios',
			'pg_ind_text_mejor_valor_todos':'...los mejor valorados por todos los usuarios',
			'pg_ind_tit_selec_mas_jugados':'Más Jugados',
			'pg_ind_tit_selec_mejor_valorados':'Mejor Valorados',
			
			'pg_ind_tit_selec_todos_juegos':' : Todos los juegos',
			'pg_ind_tit_selec_ya_jugados':' : Jugados antes por ti',
			'pg_ind_tit_selec_no_jugados':' : Aún no has jugado',
			
			'pg_ind_text_mas_vistos_archive':'...los más vistos en archive.org',
			'pg_ind_text_mas_stars_archive':'...con más stars en archive.org',
			'pg_ind_text_mas_comments_archive':'...con más comentarios en archive.org',
			'pg_ind_tit_selec_mas_vistos':'Más Vistos en archive.org',
			'pg_ind_tit_selec_mas_stars':'Con más stars en archive.org',
			'pg_ind_tit_selec_mas_comments':'Con más comentarios en archive.org',
			
			'pg_ind_text_busqueda':'...los resultados de tu búsqueda',
			'pg_ind_tit_selec_busqueda':'Busqueda',
			
			'tira_juego_juega':'juega en su web',
			'tira_juego_tu_valoracion':'tu valoración',
			
			'iframe_cerrar':'Cerrar Juego',
			
			'paginacion_pagina':'página',
			'paginacion_de':'de',
			'paginacion_inicio':'inicio',
			'paginacion_final':'final',
			'paginacion_anterior':'anterior',
			'paginacion_siguient':'siguiente',

			'introd_1':'Retrogaming Recommender',
			'introd_2':'Commodore 64',
			'introd_3':'Podrás ver más de 10.000 juegos de la mítica commodore 64',
			'introd_4':'Dispondrás de predicciones de los juegos que mejor se adaptan a tu trayectoria de juego',
			'introd_5':'Puntua cada juego según tu preferencias. Lista y busca juegos según han sido puntuados en Retrogaming o en Archive.org',
			'introd_6':'La lista de juegos está basada en los que se encuetran disponibles en web archive.org'
			},
		'fr' : 
			{'sesion_leng':'fr',
			
			'menu_inicio':'Accueil',
			'menu_favoritos':'Favori',
			'menu_en_retrogaming':'sur Retrogaming',
			'menu_en_archive':'sur Archive.org',
			'menu_todos_juegos':'Tous les jeux',
			'menu_ya_jugados':'Vous avez déjà joué',
			'menu_no_has_jugado':'Vous n\'avez pas joué',
			'menu_mas_vistos':'Les plus vues',
			'menu_mas_stars':'Plus Stars',
			'menu_mas_comments':'Plus Comments',
			'menu_mas_jugados':'Plus Joué',
			'menu_mejor_valorados':'Mieux Notés',
			'menu_busqueda':'Recherche',
			'menu_login':'Login',
			'menu_logout':'Logout',
			
			'saludo':'Salut!',
			
			'pg_login_iniciar_sesion':'Commencer Session',
			'pg_login_usuario':'Nom Utilisateur',
			'pg_login_contras':'Mot de Passe',
			'pg_login_recordarme':'Rappeler',
			'pg_login_iniciar':'Commencer Session',
			'pg_login_nuevo_user':'Nouvel Utilisateur?',
			'pg_login_click_reg':'Cliquez pour vous Inscrire!',
			'pg_login_error1':'[ Valeur Obligatoire ]',
			'pg_login_men_error_base':'S\'il vous plait, Veuillez vous connecter pour accéder à cette page.',
			'pg_login_error_ident':'Nom d\'utilisateur ou mot de passe incorrect',
			
			'pg_reg_registro':'Inscription',
			'pg_reg_usuario':'Utilisateur',
			'pg_reg_email':'Email',
			'pg_reg_contrasena':'Mot de Passe',
			'pg_reg_repe_contr':'Répéter Mot de Passe',
			'pg_reg_registrar':'Inscription',
			'pg_reg_registro_ok':'Félicitations, vous êtes déjà un utilisateur enregistré!',
			'pg_reg_error_user':'[ Utilisez un nom d\'utilisateur différent ]',
			'pg_reg_error_email':'[ Email non valide ]',
			'pg_reg_error_contrasena':'[ Mot de passe non valide ]',
			'pg_reg_error_contrasena_rep':'[ La valeur doit correspondre au mot de passe ] ',

			'pg_ind_text':'...nous pensons que cela vous plaira',
			'pg_ind_tit_selec_modelos':'Modelos',
			'pg_ind_tit_selec_usuarios':'Usuarios',
			'pg_ind_tit_selec_productos':'Productos',
			
			'pg_ind_text_favoritos':'...vos jeux préférés',			
			'pg_ind_tit_selec_favoritos':'Favoris',
			
			'pg_ind_text_mas_jugados_todos':'...le plus joué par tous les utilisateurs',
			'pg_ind_text_mejor_valor_todos':'...le mieux noté par tous les utilisateurs',
			
			
			'pg_ind_tit_selec_mas_jugados':'Plus Joué',
			'pg_ind_tit_selec_mejor_valorados':'Mieux Notés',

			'pg_ind_tit_selec_todos_juegos':' : Tous les jeux',
			'pg_ind_tit_selec_ya_jugados':' : Joué devant vous',
			'pg_ind_tit_selec_no_jugados':' : Vous n\'avez pas encore joué',
			
			'pg_ind_text_mas_vistos_archive':'...les plus vues sur archive.org',
			'pg_ind_text_mas_stars_archive':'...avec plus d\'étoiles sur archive.org',
			'pg_ind_text_mas_comments_archive':'...avec plus de commentaires sur archive.org',
			
			'pg_ind_tit_selec_mas_vistos':'Plus vu archive.org',
			'pg_ind_tit_selec_mas_stars':'Avec plus stars sur archive.org',
			'pg_ind_tit_selec_mas_comments':'Avec plus comentarios sur archive.org',
			
			'pg_ind_text_busqueda':'...les résultats de votre recherche',
			'pg_ind_tit_selec_busqueda':'Recherche',
			
			'tira_juego_juega':'jouer sur le web',
			'tira_juego_tu_valoracion':'votre évaluation',
			
			'iframe_cerrar':'Fermer Jeu',
			
			'paginacion_pagina':'page',
			'paginacion_de':'de',
			'paginacion_inicio':'début',
			'paginacion_final':'final',
			'paginacion_anterior':'précédent',
			'paginacion_siguient':'suivant',

			'introd_1':'Retrogaming Recommender',
			'introd_2':'Commodore 64',
			'introd_3':'Vous pouvez voir plus de 10 000 jeux du légendaire commodore 64',
			'introd_4':'Vous aurez des prédictions sur les jeux qui conviennent le mieux à votre trajectoire de jeu.',
			'introd_5':'Marquez chaque jeu en fonction de vos préférences. Listez et recherchez les jeux tels qu\'ils ont été évalués dans Retrogaming ou sur Archive.org',
			'introd_6':'La liste des jeux est basée sur ceux disponibles sur web archive.org'
			},
		'rm' : 			
			{'sesion_leng':'rm',
			
			'menu_inicio':'Inicio',
			'menu_favoritos':'Favoritos',
			'menu_en_retrogaming':'en Retrogaming',
			'menu_en_archive':'en Archive.org',
			'menu_todos_juegos':'Todos los Juegos',
			'menu_ya_jugados':'Ya has jugado',
			'menu_no_has_jugado':'No has jugado',
			'menu_mas_vistos':'Mas Vistos',
			'menu_mas_stars':'Mas Stars',
			'menu_mas_comments':'Mas Comments',
			'menu_mas_jugados':'Mas Jugados',
			'menu_mejor_valorados':'Mejor Valorados',
			'menu_busqueda':'Búsqueda',
			'menu_login':'Inicio Sesión',
			'menu_logout':'Salir',
			
			'saludo':'Hola!',
			
			'pg_login_iniciar_sesion':'Iniciar Sesion',
			'pg_login_usuario':'Nombre Usuario',
			'pg_login_contras':'Contraseña',
			'pg_login_recordarme':'Recordarme',
			'pg_login_iniciar':'Iniciar Sesión',
			'pg_login_nuevo_user':'Nuevo Usuario?',
			'pg_login_click_reg':'Click para Registrarse!',
			'pg_login_error1':'[ Valor Requerido ]',
			'pg_login_men_error_base':'Por favor, identifíquese para acceder a esta página.',
			'pg_login_error_ident':'Nombre de usuario o contraseña erronea',
			
			'pg_reg_registro':'Registro',
			'pg_reg_usuario':'Usuario',
			'pg_reg_email':'Email',
			'pg_reg_contrasena':'Contraseña',
			'pg_reg_repe_contr':'Repetir Contraseña',
			'pg_reg_registrar':'Registrar',
			'pg_reg_registro_ok':'Felicidades, ya eres un usuario registrado!',
			'pg_reg_error_user':'[ Use un nombre de usuario diferente]',
			'pg_reg_error_email':'[ Email no valido ]',
			'pg_reg_error_contrasena':'[ Contraseña no valida ]',
			'pg_reg_error_contrasena_rep':'[ El valor debe coincidir con la contraseña ] ',

			'pg_ind_text':'...pensamos que te gustará',
			'pg_ind_tit_selec_modelos':'Modelos',
			'pg_ind_tit_selec_usuarios':'Usuarios',
			'pg_ind_tit_selec_productos':'Productos',
			
			'pg_ind_text_favoritos':'...tus juegos favoritos',			
			'pg_ind_tit_selec_favoritos':'Favoritos',
			
			'pg_ind_text_mas_jugados_todos':'...los más jugados por todos los usuarios',
			'pg_ind_text_mejor_valor_todos':'...los mejor valorados por todos los usuarios',
			
			
			'pg_ind_tit_selec_mas_jugados':'Más Jugados',
			'pg_ind_tit_selec_mejor_valorados':'Mejor Valorados',

			'pg_ind_tit_selec_todos_juegos':' : Todos los juegos',
			'pg_ind_tit_selec_ya_jugados':' : Jugados antes por ti',
			'pg_ind_tit_selec_no_jugados':' : Aún no has jugado',
			
			'pg_ind_text_mas_vistos_archive':'...los más vistos en archive.org',
			'pg_ind_text_mas_stars_archive':'...con más stars en archive.org',
			'pg_ind_text_mas_comments_archive':'...con más comentarios en archive.org',
			
			'pg_ind_tit_selec_mas_vistos':'Más Vistos en archive.org',
			'pg_ind_tit_selec_mas_stars':'Con más stars en archive.org',
			'pg_ind_tit_selec_mas_comments':'Con más comentarios en archive.org',
			
			'pg_ind_text_busqueda':'...los resultados de tu búsqueda',
			'pg_ind_tit_selec_busqueda':'Busqueda',
			
			'tira_juego_juega':'juega en su web',
			'tira_juego_tu_valoracion':'tu valoración',
			
			'iframe_cerrar':'Cerrar Juego',
			
			'paginacion_pagina':'página',
			'paginacion_de':'de',
			'paginacion_inicio':'inicio',
			'paginacion_final':'final',
			'paginacion_anterior':'anterior',
			'paginacion_siguient':'siguiente',

			'introd_1':'Retrogaming Recommender',
			'introd_2':'Commodore 64',
			'introd_3':'Podrás ver más de 10.000 juegos de la mítica commodore 64',
			'introd_4':'Dispondrás de predicciones de los juegos que mejor se adaptan a tu trayectoria de juego',
			'introd_5':'Puntua cada juego según tu preferencias. Lista y busca juegos según han sido puntuados en Retrogaming o en Archive.org',
			'introd_6':'La lista de juegos está basada en los que se encuetran disponibles en web archive.org'
			}
		}
	
	return diccionario_todos_lenguajes

	
def carga_dicc_lenguaje(lenguaje):
	dicc_total = crea_dicc_lenguajes()
	return dicc_total[lenguaje]