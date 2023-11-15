from django.urls import path
from . import views


urlpatterns = [
    path("customers/create/", views.CustomerCreateAPIView.as_view()),
    path("customers/get/<int:customer_id>/", views.CustomerReceiveAPIView.as_view()),
    path("customers/list/", views.CustomerListAPIView.as_view()),
]
