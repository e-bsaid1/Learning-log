"""
Prends une information à partir d'une demande,
prépare les données génératrices de page, 
envoie les données au navigateur en utilisant une template 
(définit l'apparence de la page)
"""

# render : importe la fonction render(), qui effectue le rendu de la
## réponse en fonction des données fournies par les vues.
# redirect : importe la fonction redirect(), qui redirige l'utilisateur à la page topics 
## après qu'il ait posté son topic

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 

from .models import Topic, Entry #Importation des models Topic et Entry de models.py
from .forms import TopicForm, EntryForm #Importation des formulaires Topic et Entry de forms.py
from django.http import Http404 # Importation de l'exception HTTP404, erreur standar qui est retourné quand une ressource demandé n'existe pas ds un serveur 

def index(request):
	"""The home page for Learning Log."""
	return render(request, 'learning_logs/index.html') #rend la réponse inspiré des données fournis par les vues
													   #Deux arguments:
													   ##1) request : l'objet request original 

@login_required # decorateur qui vérifie si un utilisateur est connecté AVANT l'exécution de la fonction topics.
				## Si l'utilisateur n'est pas connecté, il est redirigé à la page de connexion  													   
def topics(request): #request = objet requête reçu du serveur 
	"""Show all topics."""
	topics = Topic.objects.filter(owner=request.user).order_by('date_added') # assignation des données des objets Topic, trié par dates et visible seulement par le créateur 
	context = {'topics':topics}# dictionnaire où les clés sont des noms utilisés dans le template pour accéder aux données voulues (ici topic) 
	return render(request, 'learning_logs/topics.html', context)#construction de la page 													   
																##2) un modèle utilisé par Django pour construire la page

@login_required
def topic(request, topic_id): #topic id = partie de l'URL venant après /topics/
	"""Show a single topic and all its entries."""
	topic = Topic.objects.get(id=topic_id) #requete qui récupère le topic
	# Make sure the topic belongs to the current user. 
	if topic.owner != request.user:
		raise Http404

	entries = topic.entry_set.order_by('-date_added') #requête qui prend les entrées associés au topics, chronologiq-t
	context = {'topic': topic, 'entries': entries}
	return render(request, 'learning_logs/topic.html', context) #stocke le topic et entrées dans un dict context et le retourne dans topic.html

@login_required
def new_topic(request):
	"""Add a new topic."""
	if request.method != 'POST': #si la requête est de type GET 
		# No data submitted; create a blank form
		form = TopicForm() #Utilisation de la classe TopicForm

	else: #si la requête est de type POST 
		#POST data submitted; process data.
		form = TopicForm(data=request.POST) #Contient l'information entrée par l'utilisateur 
		if form.is_valid():#Si les types de champs utilisés sont en accord avec les données, sauvegarder ces derniers
			new_topic = form.save(commit=False) #modifie le nouveau sujet avant de le passer à la base de données (BDD)
			new_topic.owner = request.user #règle la propriété du nouveau topic à l'utilisateur actuel 
			new_topic.save() #sauvegarde sur le topic défini
			return redirect('learning_logs:topics')#redirection du navigateur utilisateur vers la page topics 

	# Display a blank or invalid form. 
	context = {'form': form} #dictionnaire où est envoyé le formulaire pour l'envoyer au template
	return render(request, 'learning_logs/new_topic.html', context)
	
@login_required
def new_entry(request, topic_id):
	"""Add a new entry for a particular topic."""
	topic = Topic.objects.get(id=topic_id)#Topic relevé pour faire un rendu de la page et enclencher un processus dans les données des formulaires
	
	if request.method != 'POST': # Si la méthode de requête est GET, il ne doit rien y avoir dans le formulaire Entry
		#No data submitted; create a blank form. 
		form = EntryForm() 
	else: 
		# POST data submitted; process data.
		form = EntryForm(data=request.POST) 
		if form.is_valid():
			new_entry = form.save(commit=False)#Création d'un objet pour une nouvelle entry, sans sauvegarde
			new_entry.topic = topic #attribut opic de new_entry affecté au topic que nous avons tiré de la base de donnée au début de la fonction 
			new_entry.save() #sauvegarde de l'entry à la database avec le topic correctement associé 
			return redirect('learning_logs:topic', topic_id=topic_id) #A besoin de deux arguments : le nom de la vue que l'on veut rediriger et l'argumet dont la fonction vue requiert

	# Display a blank or invalid form. 
	context = {'topic':topic, 'form': form}
	return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
	"""Edit an existing entry."""
	entry = Entry.objects.get(id=entry_id) #Affectaion de l'entrée-objet que l'utilisateur veut éditer 
	topic = entry.topic #Affectation du topic associé avec ette entrée 
	# Si le propriétaire du topic n'est pas l'utilisateur qui tente d'éditer, élever une erreur
	if topic.owner != request.user:
		raise Http404

	if request.method != 'POST':
		#Initial request; pre-fill form with the current entry. 
		form = EntryForm(instance=entry) #Crée le formulaire pré-rempli avec les informations tiré de entry

	else:
		#POST data submitted; process data. 
		form = EntryForm(instance=entry, data=request.POST) #Crée un formulaire basé sur les informations associé avec entry
															#mis à jour avec n'importe quelle donnée pertinente partant de request.POST 
		if form.is_valid(): 
			# Si le formulaire est valide, sauvegarder et rediriger vers la page HTML topic, l'entrée mis à jour
			form.save() 
			return redirect('learning_logs:topic', topic_id=topic.id)

	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'learning_logs/edit_entry.html', context)

	