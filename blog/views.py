from django.shortcuts import render
# from django.http import HttpResponse


def posts(request):
    return render(request, 'personal/home.html')

