from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def doggy(request):
    return render(request, 'doggygo.html')

def woofcatgo(request):
    return render(request, 'foxygo.html')