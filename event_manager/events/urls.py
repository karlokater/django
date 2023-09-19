""" 
Events URLs
"""
from django.urls import path 
from . import views

app_name = "events"

urlpatterns = [
    # http://example.com/events/beispiel
    path("beispiel", views.test, name="test"),

    # Übersicht der Kategorien. http://example.com/events/categories
    path("categories", views.categories, name="categories"),

    # Detailseite der Kategorie 3. http://example.com/events/category/3
    path("category/<int:pk>", views.category_detail, name="category_detail"),
    
]

