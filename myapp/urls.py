from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),
    path('hello', views.hello),
    path('db', views.db),
]