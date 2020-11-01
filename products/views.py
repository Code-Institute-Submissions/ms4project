from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models.functions import Lower
from django.db.models import Q
from .models import Beer, Style, Brewery


def all_breweries(request):
    breweries = Brewery.objects.all()

    context = {
        'breweries': breweries
    }
    return render(request, 'products/breweries.html', context)


def all_styles(request):
    styles = Style.objects.all()

    context = {
        'styles': styles
    }
    return render(request, 'products/styles.html', context)


def all_beers(request):
    ''' A view to return beers, including sorting and search queries '''

    beers = Beer.objects.all()
    query = None
    styles = None
    breweries = None
    sort = None
    direction = None
    sortkey = None

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
            breweries = request.GET['brewery'].split(',')
            beers = beers.filter(brewery__name__in=breweries)
            breweries = Brewery.objects.filter(name__in=breweries)

        if 'style' in request.GET:
            styles = request.GET['style'].split(',')
            beers = beers.filter(style__name__in=styles)
            styles = Style.objects.filter(name__in=styles)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'Your search did\
                                not return any results, please try again')
                return redirect(reverse('beers'))

            queries = Q(name__icontains=query) |\
                Q(description__icontains=query)
            beers = beers.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'beers': beers,
        'search_term': query,
        'current_styles': styles,
        'current_breweries': breweries,
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
