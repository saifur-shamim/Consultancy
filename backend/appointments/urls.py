from django.urls import path
from .views import BookAppointmentView, MyAppointmentsView, AppointmentStatusUpdateView

urlpatterns = [
    path("book/", BookAppointmentView.as_view()),
    path("my/", MyAppointmentsView.as_view()),
    path("<int:pk>/status/", AppointmentStatusUpdateView.as_view()),
]
