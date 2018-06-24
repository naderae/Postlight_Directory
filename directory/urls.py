"""directory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from employees import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^employees/$', views.employee_list, name='employee_list'),
    url(r'^employees/create/$', views.employee_create, name='employee_create'),
    # to refer to the employee instance, we can use the pk of the object and have it in the url
    url(r'^employees/(?P<pk>\d+)/update/$', views.employee_update, name='employee_update'),
    # do the same thing to grab the employee you want to delete
    url(r'^employees/(?P<pk>\d+)/delete/$', views.employee_delete, name='employee_delete'),
]
