from django.shortcuts import render_to_response


def home(request):
    return render_to_response('home.html')


def login(request):
    return render_to_response('login.html')
