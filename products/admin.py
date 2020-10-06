from django.contrib import admin
from .models import Beer, Style, Brewery

admin.site.register(Beer)
admin.site.register(Brewery)
admin.site.register(Style)
