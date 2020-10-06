from django.shortcuts import render
from .models import Beer


def all_beers(request):
    ''' A view to return beers, including sorting and search queries '''

    beers = Beer.objects.all()

    context = {
        'beers': beers,
    }

    return render(request, 'products/beers.html', context)
