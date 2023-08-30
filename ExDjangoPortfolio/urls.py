"""
URL configuration for ExDjangoPortfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from jobs import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # WHAT DOES THIS MEAN? -->
    #   'Chris': Files the URL namespace immediately after the site's ".com"
    #       Ex: www.mydomain.com/chris
    #   'jobs.views.chris': This tells django where the intended target view
    #                       is located.
    #       Ex: jobs app folder, the views.py module, the "chris" function
    #   'name='chris'": This is a URL pass that will make referencing this page
    #                   easier in the future
    path('chris', views.chris, name='chris'),
]
