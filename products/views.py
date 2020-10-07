from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Beer


def all_beers(request):
    ''' A view to return beers, including sorting and search queries '''

    beers = Beer.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('beers'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            beers = beers.filter(queries)

    context = {
        'beers': beers,
        'search_term': query,
    }

    return render(request, 'products/beers.html', context)


def beer_detail(request, beer_id):
    ''' A view to details of specified beer '''

    beer = get_object_or_404(Beer, pk=beer_id)

    context = {
        'beer': beer,
    }

    return render(request, 'products/beer_detail.html', context)
