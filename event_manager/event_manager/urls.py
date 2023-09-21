"""
PROJEKT URLs
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", include("pages.urls")),
    path('admin/', admin.site.urls),
    path("events/", include("events.urls")),
    path("todos/", include("todo.urls")),
    path("accounts/login/",
         auth_views.LoginView.as_view(
             redirect_authenticated_user=True
         ), name="login"),
    path("accounts/", include("django.contrib.auth.urls")),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
