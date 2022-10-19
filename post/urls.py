"""fortraveler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'post'

urlpatterns = [
    path('', views.show_post),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='before_register'),
    path('login/register/', views.register, name='after_register'),
    path('post/', views.PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', views.show_post_detail),
    path('upload/',csrf_exempt(views.Uploadfile.as_view()), name='upload')
    
]
