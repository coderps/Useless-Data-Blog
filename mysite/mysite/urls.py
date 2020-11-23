"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from uselessdata import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    url(r'^experiments/$', views.experiments, name='experiments'),
    url(r'^experiments/effects-of-gravity-on-height/$', views.blog1, name='blog1'),
    url(r'^experiments/effects-of-gravity-on-height/success$', views.success1, name='success'),
    url(r'^experiments/life-spent-on-daily-activities/$', views.blog2, name='blog2'),
    url(r'^experiments/life-spent-on-daily-activities/success2$', views.success2, name='success2'),
    url(r'^contact-us/$', views.contact, name='contact'),
    url(r'^contact-us/recorded$', views.recorded, name='recorded'),
    url(r'^bets/$', views.bets, name='bets'),
    url(r'^donate/$', views.bets, name='donate')
]
