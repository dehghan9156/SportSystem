from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'race'

urlpatterns = [
    path('api/v1/',include('race.api.v1.urls',namespace='api-v1'),),
]