from django.shortcuts import get_object_or_404
from decimal import Decimal
from django.conf import settings
from products.models import Beer


def cart_contents(request):

    cart_items = []
    total = 0
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

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'beer_count': beer_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
