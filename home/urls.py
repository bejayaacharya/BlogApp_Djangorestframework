
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('blog/',BlogView.as_view()),
    
]
