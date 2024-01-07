from django.contrib import admin
# the created database in models.py needs to be registered in this admin.py
from .models import Feature
# Register your models here.

admin.site.register(Feature)
