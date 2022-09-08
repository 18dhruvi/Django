from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('register/', views.Register, name='register'),
    path('blogs/',views.blogs, name='blogs'),
    path('login/', views.Login, name='login'),
    path('logout',views.logout, name='logout'),
    path('profile/', views.profile,name='profile'),
    path('blogpost/',views.blogpost, name='blogpost'),
]
