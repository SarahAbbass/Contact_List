from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'list/contact_list.html', {'contacts': contacts})


def add_contact(request):
    #error_message = None
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_instance = form.save(commit=False)
            if contact_instance.error_message:
                return render(request, 'error.html', {'error_message': contact_instance.error_message})
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'list/contact_form.html', {'form': form})


def edit_contact(request, pk):
    contact = Contact.objects.get(pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'list/contact_form.html', {'form': form})


def delete_contact(request, pk):
    contact = Contact.objects.get(pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'list/delete_contact.html')


#def success(request):
    #return render(request, 'list/success.html')
