from django.urls import path
from . import views

urlpatterns = [
    path('reminders/', views.ReminderCreateView.as_view(), name='create-reminder'),
]