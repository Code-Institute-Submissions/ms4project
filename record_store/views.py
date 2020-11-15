from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Record
from .forms import RecordForm


def all_records(request):
    records = Record.objects.all()

    context = {
        'records': records
    }

    return render(request, 'records/records.html', context)


@login_required
def add_record(request):
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, you are not authorised to edit records')
        return redirect(reverse('records'))

    ''' Add a record to the collection '''
    if request.method == 'POST':
        form = RecordForm(request.POST, request.FILES)
        if form.is_valid():
            record = form.save()
            messages.success(request, 'Added record to store!')
            return redirect(reverse('record', args=[record.id]))
        else:
            messages.error(request,
                           'Record not added, please try again.')
    else:
        form = RecordForm()

    template = 'records/add_record.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_record(request, record_id):
    ''' edit a record form the collection '''
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, you are not authorised to edit collection')
        return redirect(reverse('records'))

    record = get_object_or_404(Record, pk=record_id)
    if request.method == 'POST':
        form = RecordForm(request.POST, request.FILES, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record update successful!')
            return redirect(reverse('records', args=[record.id]))
        else:
            messages.error(request, 'Update failed, please try again.')
    else:
        form = RecordForm(instance=record)
        messages.info(request,
                      f'Currently editing {record.title} by {record.artist}')

    template = 'records/edit_record.html'
    context = {
        'form': form,
        'record': record,
    }

    return render(request, template, context)


@login_required
def delete_record(request, record_id):
    ''' remove record from collection '''
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, you are not authorised to edit collection')
        return redirect(reverse('record'))

    record = get_object_or_404(Record, pk=record_id)
    record.delete()
    messages.success(request, 'Record removed from collection')
    return redirect(reverse('records'))
