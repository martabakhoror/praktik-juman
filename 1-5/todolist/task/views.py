from django.shortcuts import render
from django.http import  HttpResponse

from . import models

# Create your views here.
def index(req) :
    if req.POST:
        models.Task.objects.create(nama=req.POST["nama"])
        return redirect ('/')

    tasks=models.Task.objects.all()
    return render (req, 'index.html', {
        'data': tasks 
    })
  
