from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('search', views.search, name="search"),
    path('catSearch', views.catSearch, name="catSearch"),
    path('autoSearch', views.autoSearch, name="autoSearch")
]