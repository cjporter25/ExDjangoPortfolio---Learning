from django.contrib import admin

# ".models" tells python to import directly from the "models.py" module inside
#       the same directory
# We are importing "Job" as that is the name of the model class made in models.py
from .models import Job

# Register your models here.
admin.site.register(Job)
