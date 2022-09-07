from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('register', views.Register, name='register'),
    path('blogs',views.blogs, name='blogs'),
]
