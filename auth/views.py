from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    # logging business logic, to be run here
    return render(
        request,
        "signin.html"
    )

def logout(request):
    return render(
        request,
        "logout.html"
    )