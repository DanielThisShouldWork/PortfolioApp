from django.shortcuts import render

def home(request):
    return render(request, 'portfolioapp/home.html')

def about(request):
    return render(request, 'portfolioapp/about.html')

def projects(request):
    return render(request, 'portfolioapp/projects.html')

def contacts(request):
    return render(request, 'portfolioapp/contacts.html')