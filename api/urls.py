from django.contrib import admin
from django.urls import path , include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from . import views



router = routers.DefaultRouter()

# add route path
router.register('labels' , views.LabelViewSet)
router.register('tasks' , views.TaskViewSet)



urlpatterns = [
    path('' , include(router.urls))
]
