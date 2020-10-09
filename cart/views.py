from django.shortcuts import render, redirect
# get_object_or_404
# from products.models import Beer


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
