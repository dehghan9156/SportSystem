from django.contrib import admin
from django.urls import path,include
from . import views

app_name="api-v1"

urlpatterns = [
    path("test/",views.TestView.as_view(),name="test")
]
