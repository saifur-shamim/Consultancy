from django.urls import path
from .views import BookAppointmentView, ConsultantAppointmentListView, AppointmentStatusUpdateView

urlpatterns = [
    path("book/", BookAppointmentView.as_view()),
    path("my/", ConsultantAppointmentListView.as_view()),
    path("status/<int:pk>/", AppointmentStatusUpdateView.as_view()),
]

