from django.shortcuts import render
from .forms import ContactForm
from .models import Contact, Producto
from django.http import HttpResponse

# Create your views here.

def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            second_name = form.cleaned_data['second_name']
            first_last_name = form.cleaned_data['first_last_name']
            second_last_name = form.cleaned_data['second_last_name']
            email_adress = form.cleaned_data['email_adress']
            number_prefix = form.cleaned_data['number_prefix']
            phone_number = form.cleaned_data['phone_number']
            comment = form.cleaned_data['comment']

            form.save()

    else:
        form = ContactForm()

    return render(request, 'formulario_contacto.html', {'form': form})

def home_template(request):
    return render(request, 'home.html', {})


def about_template(request):
    return render(request, 'about.html', {})


def contact_table_list(request):
    contact_information = Contact.objects.all()
    contexto = {
        'contact_information' : contact_information
    }

    return render(request, 'search_contacts.html', contexto)

def products_list(request):
    products = Producto.objects.all()
    rows_count = 1 + int(products.count() / 3)
    rows = []
    for row in range(0, rows_count):
        start_count = row * 4
        rows.append(products[start_count: start_count +4])
    
    contexto = {
        'product_information': rows
    }

    return render(request, 'product_list.html', contexto)
