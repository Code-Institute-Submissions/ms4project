from django.shortcuts import render, redirect, reverse, get_object_or_404,\
    HttpResponse
from django.contrib import messages
from products.models import Beer


def view_cart(request):
    ''' A view that renders shopping cart '''

    return render(request, 'cart/cart.html')


def add_to_cart(request, beer_id):
    ''' Add a quantity of a specifice beer to the cart '''

    # beer = get_object_or_404(Beer, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if beer_id in list(cart.keys()):
        cart[beer_id] += quantity
    else:
        cart[beer_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, beer_id):
    """ Adjust the quantity of a specified product to the specified amount """

    beer = get_object_or_404(Beer, pk=beer_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[beer_id] = quantity
        messages.success(request,
                         f'Updated {beer.name}\
                                 quantity to {cart[beer_id]}')
    else:
        cart.pop(beer_id)
        messages.success(request,
                         f'Removed {beer.name} from your bag')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, beer_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Beer, pk=beer_id)
        cart = request.session.get('bag', {})

        cart.pop(beer_id)
        messages.success(request,
                         f'Removed {product.name} from your bag')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item {e}')
        return HttpResponse(status=500)
