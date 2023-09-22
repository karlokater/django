from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("category", views.CategoryViewSet)
router.register("event", views.EventViewSet)
