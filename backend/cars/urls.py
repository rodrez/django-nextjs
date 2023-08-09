from django.urls import path
from . import views


urlpatterns = [
    path("", views.CarView.as_view(), name="cars"),
    path("create-car/", views.CarCreateView.as_view(), name="create-cars"),
    path("cars/", views.CarListView.as_view(), name="view-cars"),
]
