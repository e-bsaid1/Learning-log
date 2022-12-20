"""Defines URL patterns for users"""

# importe les fonctions : 
## 1) path pour router les adresses
## 2) include pour ajouter les URL d'authentification par défaut que Django a défini
from django.urls import path, include 

#importe à partir de users les modules views pour écrire notre propre view pour la page d'inscription
from . import views


app_name = 'users' #variable permettant à Django de distinguer les URL patterns pour l'utilisateur des URL 
				   #appartenant à d'autres applications (ex : learning_log)
urlpatterns = [
	# Include default auth urls. 
	path('', include('django.contrib.auth.urls')),# colle à l'URL http://localhost:8000/users/login
												  ## users : demande à Django de regarder dans users/urls.py
												  ## login : appelle Django à envoyer des requêtes à la vue login par défaut du framework
	# Registration page. 
	path('register/', views.register, name='register'), # colle à l'URL http://localhost:8000/users/registers											  
														# envoie des requêtes à la fonction register() que nous avons écrit 
								
] 

