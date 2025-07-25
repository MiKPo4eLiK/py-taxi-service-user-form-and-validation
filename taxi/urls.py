from django.urls import path
from .views import assign_me_to_car, delete_me_from_car

from .views import (
    index,
    CarListView,
    CarDetailView,
    CarCreateView,
    CarUpdateView,
    CarDeleteView,
    DriverListView,
    DriverDetailView,
    DriverCreateView,
    DriverDeleteView,
    DriverLicenseUpdateView,
    ManufacturerListView,
    ManufacturerCreateView,
    ManufacturerUpdateView,
    ManufacturerDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list",
    ),
    path(
        "manufacturers/create/",
        ManufacturerCreateView.as_view(),
        name="manufacturer-create",
    ),
    path(
        "manufacturers/<int:pk>/update/",
        ManufacturerUpdateView.as_view(),
        name="manufacturer-update",
    ),
    path(
        "manufacturers/<int:pk>/delete/",
        ManufacturerDeleteView.as_view(),
        name="manufacturer-delete",
    ),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("cars/create/", CarCreateView.as_view(), name="car-create"),
    path("cars/<int:pk>/update/", CarUpdateView.as_view(), name="car-update"),
    path("cars/<int:pk>/delete/", CarDeleteView.as_view(), name="car-delete"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    ),
    path(
        "drivers/create/", DriverCreateView.as_view(), name="driver-create"
    ),
    path(
        "drivers/<int:pk>/delete/", DriverDeleteView.as_view(), name="driver-delete"
    ),
    path(
        "drivers/<int:pk>/update_license/",
        DriverLicenseUpdateView.as_view(),
        name="driver-license-update"
    ),
    path(
        "cars/<int:pk>/assign_me/", assign_me_to_car, name="car-assign-me"
    ),
    path(
        "cars/<int:pk>/delete_me/", delete_me_from_car, name="car-delete-me"
    ),

]

app_name = "taxi"
