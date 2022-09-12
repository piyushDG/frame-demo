from django.contrib import admin
from django.urls import path, include
from farmer_scorecard_api.views import Kharif1Paddy2021_oneViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('',Kharif1Paddy2021_oneViewSet)

urlpatterns = router.urls
