from django.db import models

# Create your models here.
# Model = class

class Topic(models.Model):#Which inherit from Model, parent class included in Django
						  #defines the basic functionality of a model. 
	"""A topic the user is learning about"""
	text = models.CharField(max_length=200)#Piece of data made of characters with a limit 
	date_added = models.DateTimeField(auto_now_add=True)#Piece of data which record
														#date and time													
	def __str__(self):#Attribute used by default when there is information about a topic
		"""Return a string representation of the model."""
		return self.text

class Entry(models.Model):
	"""Something specific learned about a topic"""
	topic = models.ForeignKey(Topic, on_delete = models.CASCADE)#Connect to each entry to a specific topic
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)#Present entries in chronological order

	class Meta:#Holds extra information for managing a model
		verbose_name_plural = 'entries'

	def __str__(self):
		"""Return a string representation of the model"""
		if len(self.text)> 50:#Si le texte a plus de 50 caractères ajouter une ellipse après les 50 1er charactères
			return self.text[:50] + "..."#Show just the first 50 character of text

		else: #Sinon tout retourner 
			return self.text






