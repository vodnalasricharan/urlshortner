from django.urls import path
from . import views
urlpatterns = [
    path("", views.createurl, name="home"),
    path("<str:slugs>/", views.urlRedirect, name="redirect")
]