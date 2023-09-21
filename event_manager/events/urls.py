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

    # Kategorie eintragen. http://example.com/events/category/add
    path("category/add", views.category_add, name="category_add"),

    # Übersicht der Events: http://example.com/events
    path("", views.EventListView.as_view(), name="events"),

    # Detailseite des Events: http://example.com/events/3
    path("<int:pk>", views.EventDetailView.as_view(), name="event_detail"),
    path("create", views.EventCreateView.as_view(), name="event_create"),
    path("update/<int:pk>", views.EventUpdateView.as_view(), name="event_update"),

    # events/getdata
    path("getdata", views.get_data, name="get_data"),
    path("search", views.EventSearchView.as_view(), name="search"),
]
