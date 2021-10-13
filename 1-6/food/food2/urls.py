
from django.urls import path
from . import views
urlpatterns = [

    path('', views.home),
    path('tambah/', views.tambah),  # / unruk meneruskan ke link selanjutnya
    path('<id>/delete/', views.delete),
    path('<id>/update/', views.update),
    path('<id>/detail/', views.detail),

]
