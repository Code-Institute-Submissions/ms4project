from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models.functions import Lower
from django.db.models import Q
from .models import Beer, Style, Brewery


def all_beers(request):
    ''' A view to return beers, including sorting and search queries '''

    beers = Beer.objects.all()
    query = None
    style = None
    brewery = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                beers = beers.annotate(lower_name=Lower('name'))
            if sortkey == 'style':
                sortkey = 'style__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
        beers = beers.order_by(sortkey)

        if 'brewery' in request.GET:
            brewery = request.GET['brewery'].split(',')
            beers = beers.filter(brewery__name__in=brewery)
            brewery = Brewery.objects.filter(name_in=brewery)

        if 'style' in request.GET:
            style = request.GET['style'].split(',')
            beers = beers.filter(style__name__in=style)
            style = Style.objects.filter(name_in=style)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('beers'))

            queries = Q(name__icontains=query) |\
                Q(description__icontains=query)
            beers = beers.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'beers': beers,
        'search_term': query,
        'style': style,
        'brewery': brewery,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/beers.html', context)


def beer_detail(request, beer_id):
    ''' A view to details of specified beer '''

    beer = get_object_or_404(Beer, pk=beer_id)

    context = {
        'beer': beer,
    }

    return render(request, 'products/beer_detail.html', context)
