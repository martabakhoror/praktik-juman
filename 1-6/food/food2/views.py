from django.http import request
from django.shortcuts import redirect, render
from . import models


def home(request):
    data = models.Task.objects.all()  # all untuk mengambil semuanya
    return render(request, 'home.html', {
        'data': data,
    })


def tambah(request):
    if request.POST:  # fungsi post itu untuk menambahkan data
        models.Task.objects.create(
            item=request.POST['item'],
            # list data yang akan di tambahkan. harga pertana kembali ke models,harga yang ke dua kembali ke template
            harga=request.POST['harga']
        )
        return redirect('/')
  # ketika berhasil nanti kembali ke fungsi itu
    data = models.Task.objects.all()  # all untuk mengambil semuanya
    return render(request, 'tambah.html', {  # dalam tanda petik merupakan template
        'data': data,
    })


def delete(request, id):
    models.Task.objects.filter(pk=id).delete()  # pk = primary key
    return redirect('/')


def update(request, id):
    if request.POST:
        models.Task.objects.filter(pk=id).update(
            item=request.POST[item],
            harga=request.POST[harga])
        return redirect('/')

# # Create your views here.
# def index (req):
#     if request.POST :
#     models.Task.objects.create(item=request.POST['item'])
#     return redirect ('/')
#     task = models.Task.objects.all()
#     return render(req,'home.html'),{
#         'data' :task,
#     }

# def delete (request, id):
#     models.Task.object.filter(pk=id).delete()
#     return redirect ('/')

# def rincian (request,id):
#     models.Task.object.filter(pk=id).first()
#     return redirect ('/')
#     return render(req,)
