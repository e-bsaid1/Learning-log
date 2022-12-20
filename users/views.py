from django.shortcuts import render, redirect #import° des fct render() et redirect()
from django.contrib.auth import login #import° de la fonction login(), qui connecte l'utilisateur 
from django.contrib.auth.forms import UserCreationForm #permet de créer un nouvel utilisateur pour utiliser l'appli web 

# Create your views here.

def register(request):
	"""Register a new user."""
	if request.method != 'POST':
		#Display blank registration form.
		form = UserCreationForm()
	else:
		# Process completed form. 
		form = UserCreationForm(data=request.POST)

		if form.is_valid(): 
		# Si le pseudo a les bons caractères, avec les bons mdp, et sans mauvaises manips utilisateurs 
			new_user = form.save()
			# Connecte l'utilisateur et ensuite le redirige à la page d'acceuil
			login(request, new_user)
			return redirect('learning_logs:index')

	# Affiche un formulaire vide ou invalide 
	context = {'form':form}
	return render(request, 'registration/register.html', context)



