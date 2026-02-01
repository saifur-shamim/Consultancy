from django.urls import path
from .views import RegisterView, ConsultantListView, ConsultantCreateView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('consultants/', ConsultantListView.as_view()),
    path("create-consultant/", ConsultantCreateView.as_view()),

]
