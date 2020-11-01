from django.shortcuts import render

from .models import Record


def all_records(request):
    records = Record.objects.all()

    context = {
        'records': records
    }

    return render(request, 'products/records.html', context)
