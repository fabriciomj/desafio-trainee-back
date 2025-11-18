from django.urls import include, path

urlpatterns = [
    path("", include("mini_ifood.urls")),
]
