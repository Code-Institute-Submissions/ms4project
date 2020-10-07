from django.shortcuts import render, get_object_or_404
from .models import Beer


def all_beers(request):
    ''' A view to return beers, including sorting and search queries '''

    beers = Beer.objects.all()

    context = {
        'beers': beers,
    }

    return render(request, 'products/beers.html', context)


def beer_detail(request, beer_id):
    ''' A view to details of specified beer '''

    beer = get_object_or_404(Beer, pk=beer_id)

    context = {
        'beer': beer,
    }

    return render(request, 'products/beer_detail.html', context)
