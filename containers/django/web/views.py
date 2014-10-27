from django.shortcuts import render
from user.decorators import authenticated_view

@authenticated_view
def app(request):
    return render(request, 'app.html')

@authenticated_view
def about(request):
    return render(request, 'app.html')
