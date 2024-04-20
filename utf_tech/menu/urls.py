from django.urls import path
from . import views

urlpatterns = [
    path('', views.FoodList.as_view(), name='home'),
]
