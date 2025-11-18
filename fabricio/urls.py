from django.urls import include, path

urlpatterns = [
    path("", include("mini_ifood.urls")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
