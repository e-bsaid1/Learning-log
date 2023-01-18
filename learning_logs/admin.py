from django.contrib import admin

# Register your models you want to register here
from learning_logs.models import Topic, Entry

admin.site.register(Topic)#Dit à Django de gérer nos modèles à travers le site administrateur 
admin.site.register(Entry)
