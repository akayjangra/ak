from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')
def ram(request):
    data = request.GET['firstname']
    return render(request,'ram.html',{
        'data': data

    })
