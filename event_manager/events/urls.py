""" 
Events URLs
"""
from django.urls import path 
from . import views 

urlpatterns = [
    # http://example.com/ereignisse/beispiel
    path("beispiel", views.test, name="test"),
]

