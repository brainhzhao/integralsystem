from django.shortcuts import render

# Create your views here.


def to_login(request):
    return render(request,"login/login.html")