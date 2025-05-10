from django.db import models

class Reminder(models.Model):
    message = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    notification_method = models.CharField(
        max_length=5,
        choices=[('SMS', 'SMS'), ('EMAIL', 'Email')],
        default='EMAIL'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reminder: {self.message[:20]}..."
