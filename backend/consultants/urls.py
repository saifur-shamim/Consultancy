from django.urls import path
from .views import CreateAvailabilityView, ConsultantAvailabilityListView

urlpatterns = [
    path("availability/create/", CreateAvailabilityView.as_view()),
    path("availability/<int:consultant_id>/", ConsultantAvailabilityListView.as_view()),
]
