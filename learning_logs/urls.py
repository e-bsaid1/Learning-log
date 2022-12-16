"""Defines URL patterns for learning_logs."""

from django.urls import path #permet d'importer la fonction path

from . import views# permet d'importer le module views présent dans learning_logs

app_name = 'learning_logs' #permet de distinguer l'urls.py d'autres urls.py d'autres applic° ds le projet
urlpatterns = [	 
	#liste de pages individuelles demandés sur l'appli learning_logs
	path('', views.index, name='index'),#trois arguments : 
										# '' :relie l'URL demandé à une vue, remplaçant l'url de base (http://localhost:8000/) 
										# views.index : appele une fonction dans views.py (ici index()) quand l'URL demandé est trouvé 
	#Page that shows all topics. 
	path('topics/', views.topics, name ='topics'),
	# Detail page for a single topic. 
	path('topics/<int:topic_id>/', views.topic, name='topic'), #1e argument = regarde ce qui vient après les URL qui ont le mot topics et y ajoute un entier entre deux slashs
	# Page for adding a new topic
	path('new_topic/', views.new_topic, name = 'new_topic'),
	# Page for adding a new entry
	path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
	# Page for editing an entry. 
	path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]

