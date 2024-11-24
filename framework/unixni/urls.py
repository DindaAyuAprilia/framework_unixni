from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about', views.about, name='about'),
    path('tim', views.tim, name='tim'),
    path('galeri', views.galeri, name='galeri'),
    path('kontak', views.kontak, name='kontak'),
    path('daftar', views.daftar, name='daftar'),
    path('masuk', views.masuk, name='masuk'),
    path('blog', views.blog_list, name='blog'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blog/like/<int:pk>/', views.blog_like, name='blog_like'),
]