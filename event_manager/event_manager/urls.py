"""
PROJEKT URLs
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from events.api.urls import router
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularSwaggerView
from rest_framework.authtoken.views import obtain_auth_token

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
    path("api/", include(router.urls)),  # api/category

    path(
        "schema/",
        SpectacularAPIView.as_view(api_version="v2"),
        name="schema",
    ),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    # User kann per POST einen neuen Token generieren
    path("token", obtain_auth_token, name="api-token"),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
