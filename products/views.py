from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.db.models import Q
from .models import Beer, Style, Brewery
from .forms import BeerForm


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


@login_required
def add_beer(request):
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, you are not authorised to edit beer collection')
        return redirect(reverse('beers'))

    ''' Add a beer to the store '''
    if request.method == 'POST':
        form = BeerForm(request.POST, request.FILES)
        if form.is_valid():
            beer = form.save()
            messages.success(request, 'Added beer to store!')
            return redirect(reverse('beer_detail', args=[beer.id]))
        else:
            messages.error(request,
                           'Beer not added, please check form and try again.')
    else:
        form = BeerForm()

    template = 'products/add_beer.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_beer(request, beer_id):
    ''' edit a beer form the store '''
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, you are not authorised to edit beer collection')
        return redirect(reverse('beers'))

    beer = get_object_or_404(Beer, pk=beer_id)
    if request.method == 'POST':
        form = BeerForm(request.POST, request.FILES, instance=beer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Beer update successful!')
            return redirect(reverse('beer_detail', args=[beer.id]))
        else:
            messages.error(request, 'Update failed, please try again.')
    else:
        form = BeerForm(instance=beer)
        messages.info(request, f'Currently editing {beer.name}')

    template = 'products/edit_beer.html'
    context = {
        'form': form,
        'beer': beer,
    }

    return render(request, template, context)


@login_required
def delete_beer(request, beer_id):
    ''' remove beer from store '''
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, you are not authorised to edit collection')
        return redirect(reverse('beers'))

    beer = get_object_or_404(Beer, pk=beer_id)
    beer.delete()
    messages.success(request, 'Beer removed from store')
    return redirect(reverse('beers'))
