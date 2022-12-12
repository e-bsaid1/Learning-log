from django import forms 

#Usage des modèles Topic et Entry dans models.py
from .models import Topic, Entry


class TopicForm(forms.ModelForm): 
	"""Classe indiquant sur quel modèle le formulaire doit se baser et quels champs y inclure """
	class Meta: 
		model = Topic # utilisation du modèle Topic
		fields = ['text'] # inclusion du champ de texte
		labels = {'text': ''} # empêche d'utiliser des labels pour le champ de texte

class EntryForm(forms.ModelForm): 
	"""Classe indiquant sur quel modèle le formulaire doit se baser et quels champs y inclure """
	class Meta: 
		model = Entry # utilisation du modèle Topic
		fields = ['text'] # inclusion du champ de texte
		labels = {'text': 'Entry:'} # empêche d'utiliser des labels pour le champ de texte
		widgets = {'text': forms.Textarea(attrs={'cols': 80})} #un élément de formulaire HTML 
													 #(ex: boite de texte à une ligne, zone de texte à plusieurs lignes, liste déroulante)
													 #forms.Textarea(attrs={'cols': 80}) : aire de texte à 80 colonnes de large au lieu des 40 par défaut 

