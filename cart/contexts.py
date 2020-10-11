from django.shortcuts import get_object_or_404
from decimal import Decimal
from django.conf import settings
from products.models import Beer


def cart_contents(request):

    cart_items = []
    total = 0
    quantity = 0
    beer_count = 0
    cart = request.session.get('cart', {})

    for beer_id, quantity in cart.items():
        if isinstance(quantity, int):
            beer = get_object_or_404(Beer, pk=beer_id)
            total += quantity * beer.price
            beer_count += quantity
            cart_items.append({
                'beer_id': beer_id,
                'quantity': quantity,
                'beer': beer,
            })

    if quantity < 6:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    else:
        delivery = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'quantity': quantity,
        'total': total,
        'beer_count': beer_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
