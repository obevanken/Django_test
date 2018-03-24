from django.shortcuts import render


def index(request):
    return render(request, 'web/home.html')

def contacts(request):
    return render(request, 'web/contacts.html', {'values' : ['Обращайтесь по номеру', '8 800 555 3535']})
