from django.contrib import admin

# Register your models you want to register here
from learning_logs.models import Topic, Entry

admin.site.register(Topic)#Tell Django to manage our model through the admin site
admin.site.register(Entry)
