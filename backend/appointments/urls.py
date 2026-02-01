from django.urls import path
from .views import BookAppointmentView, MyAppointmentsView

urlpatterns = [
    path("book/", BookAppointmentView.as_view()),
    path("my/", MyAppointmentsView.as_view()),
]
