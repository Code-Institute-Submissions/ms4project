from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import Orderform


def checkout(request):
    cart = request.session.get('bag', {})
    if not cart:
        messages.error(request,  "Your cart is empty")
        return redirect(reverse('beers'))

    order_form = Orderform()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
