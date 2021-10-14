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
        # hargamakanan = int(request.POST['hargamakanan'])
        models.Task.objects.create(
            makanan=request.POST['makanan'],
            jenismakanan=request.POST['jenis'],
            hargamakanan=request.POST['hargamakanan'],
            minuman=request.POST['minuman'],
            # list data yang akan di tambahkan. harga pertana kembali ke models,harga yang ke dua kembali ke template
            hargaminuman=request.POST['hargaminuman']
        )
        x = request.POST['jenis']
        print(x)
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
            makanan=request.POST['makanan'],
            hargamakanan=request.POST['hargamakanan'],
            minuman=request.POST['minuman'],
            hargaminuman=request.POST['hargaminuman'])
        return redirect('/')

    data = models.Task.objects.all()  # all untuk mengambil semuanya
    return render(request, 'edit.html', {  # dalam tanda petik merupakan template
        'data': data,
    })


def detail(request, id):
    data = models.Task.objects.filter(pk=id).first()
    return render(request, 'detail.html', {
        'data': data  # mengambil value di variable data
    })

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
