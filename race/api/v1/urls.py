from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from . import views

app_name="api-v1"

router = DefaultRouter()
router.register(r'category', views.CategoryApiViewSet, basename='admin-category')
router.register(r'race', views.RaceApiViewSet,basename="admin-race")

urlpatterns = [
    path('', include(router.urls))
]