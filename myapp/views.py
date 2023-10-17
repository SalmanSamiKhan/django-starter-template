from django.shortcuts import render, HttpResponse
from myapp.models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    context = {
        'key1':'value1',
        'key2':'value2'
    }
    messages.success(request, 'This is a test message')
    return render(request, 'home.html', context)

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Create contact object of Contact class
        contact = Contact(name=name, email=email, password=password)
        contact.save()
        messages.success(request, 'Form Submitted Successfully!')
    return render(request, 'contact.html')