from django.contrib import admin
from django.urls import path,include
from Account.views import *

urlpatterns = [
   path('account/',include('Account.urls')),
    path('home/',include('home.urls'))
]
