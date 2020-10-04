"""Urls for hazards_detection project. 

Link to show dashboard.
"""
from django.urls import path
from .views import dashboard

urlpatterns = [
    path('', dashboard)
]
