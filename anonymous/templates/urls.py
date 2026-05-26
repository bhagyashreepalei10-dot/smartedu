"""
URL configuration for smartedu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from anonymous import views as anoview

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home Page
    path('', anoview.index, name='index'),
    path('index/', anoview.index, name='index'),

    # Other Pages
    path('contact/', anoview.contact, name='contact'),
    path('faq/', anoview.faq, name='faq'),
    path('gallery/', anoview.gallery, name='gallery'),
    path('about/', anoview.about, name='about'),
    path('login/', anoview.login, name='login'),
    path('register/', anoview.register, name='register'),

    # Calculator Page
    path('add/', anoview.add, name='add'),
    path('cgpa/', anoview.cgpa, name='cgpa'),

path('logbook/', anoview.logbook, name='logbook'),
path('calculator/', anoview.calculator, name='calculator'),
]



