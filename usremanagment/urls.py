from django.conf.urls import url,include
from django.contrib import admin

from usremanagment.views import GetUser

urlpatterns = [
    url(r'^login/$', GetUser.as_view(), name='home')
]
