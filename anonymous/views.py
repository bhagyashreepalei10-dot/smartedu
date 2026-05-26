from django.shortcuts import render
from django.http import HttpResponse


# Home Page
def index(request):
    return render(request, 'index.html')


# Contact Page
def contact(request):
    return render(request, 'contact.html')


# FAQ Page
def faq(request):
    return render(request, 'faq.html')


# Gallery Page
def gallery(request):
    return render(request, 'gallery.html')


# About Page
def about(request):
    return render(request, 'about.html')


# Login Page
def login(request):
    return render(request, 'login.html')


# Register Page
def register(request):
    return render(request, 'register.html')

def cgpa(request):
    return render(request,'cgpa.html')


def logbook(request):
    return render(request,'logbook.html')   

def calculator(request):
    return render(request,'calculator.html')


# Add & Subtract Calculator
def add(request):

    output = ""

    if request.method == "POST":

        f = request.POST.get('f')
        s = request.POST.get('s')
        operation = request.POST.get('operation')

        f = int(f)
        s = int(s)

        if operation == "add":
            output = f + s

        elif operation == "subtract":
            output = f - s

    return render(request, 'add.html', {'output': output})