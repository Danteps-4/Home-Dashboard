from django.contrib import admin
from .models import Person, Family

# Register your models here.
admin.site.register(Person)
admin.site.register(Family)