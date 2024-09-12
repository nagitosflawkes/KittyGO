from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('doggygo/', views.doggy),
    path('woofcatgo/', views.woofcatgo)
]