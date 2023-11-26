# fileupload/urls.py
from django.urls import path
from .views import * 

urlpatterns = [
	path('getresult/', getresult),
]