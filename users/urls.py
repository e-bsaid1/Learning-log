"""Defines URL patterns for users"""

# importe les fonctions : 
## 1) path pour router les adresses
## 2) include pour ajouter les URL d'authentification par défaut que Django a défini
from django.urls import path, include 

app_name = 'users' #variable permettant à Django de distinguer les URL patterns pour l'utilisateur des URL 
				   #appartenant à d'autres applications (ex : learning_log)
urlpatterns = [
	# Include default auth urls. 
	path('', include('django.contrib.auth.urls')),# colle à l'URL http://localhost:8000/users/login
												  # users : demande à Django de regarder dans users/urls.py
												  # login : appelle Django à envoyer des requêtes à la vue login par défaut du framework

								
] 

