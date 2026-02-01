from django.urls import path
from .views import FirmCreateView

urlpatterns = [
    path("create/", FirmCreateView.as_view()),
]
