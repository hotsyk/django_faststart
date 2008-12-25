# -*- coding: utf-8

from django.contrib import admin
from models import *

class Model1Admin(admin.ModelAdmin):
    #list_display = ['']
    pass


admin.site.register(Model1, Model1Admin)
