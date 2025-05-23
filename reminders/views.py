from rest_framework import generics
from .models import Reminder
from .serializers import ReminderSerializer  # This import should now work

class ReminderCreateView(generics.CreateAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer