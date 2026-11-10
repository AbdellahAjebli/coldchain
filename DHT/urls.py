from django.urls import path
from . import views
from .api import Dlist, Dhtviews

urlpatterns = [
    path("", views.dht_view, name="dht-home"),
    path("list/", Dlist, name="dht-list"),
    path("post/", Dhtviews.as_view(), name="dht-create"),
]
