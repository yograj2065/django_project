"""
URL configuration for mysite project.

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
from django.urls import path, include
from adcs import views
from adcs.views import home
from adcs.views import index
from adcs.views import gallery
from adcs.views import contact
from temp.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('gallery/', gallery),
    path('', include('adcs.urls')),
    path('index/', index, name='index'),
    path('contact/', contact, name='contact'),


]

urlpatterns += [
    path('home/', home, name='home'),   
    path(' ', views.home)
]
