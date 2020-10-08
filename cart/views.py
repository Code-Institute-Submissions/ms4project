from django.shortcuts import render


def view_cart(request):
    ''' A view that renders shooping cart'''
    return render(request, 'cart/cart.html')
