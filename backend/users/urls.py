from django.urls import path
from .views import RegisterView, ConsultantListView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('consultants/', ConsultantListView.as_view()),
]
