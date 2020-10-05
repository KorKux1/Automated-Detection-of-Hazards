"""Urls for hazards_detection project. 

Link to show dashboard.
"""
from django.urls import path
from .views.views_main import dashboard
from .views.views_main import air_quality

urlpatterns = [
    path('', dashboard),
    path('air-quality/<int:year>/', air_quality, name='air-quality')
]
