from django.contrib import admin
from .models import Beer, Style, Brewery


class BeerAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'style',
        'price',
        'rating',
        'volume',
        'abv',
        'image',
        'brewery',
    )

    ordering = ('sku',)


class StyleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )


class BreweryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        'country'
    )


admin.site.register(Beer, BeerAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(Brewery, BreweryAdmin)

