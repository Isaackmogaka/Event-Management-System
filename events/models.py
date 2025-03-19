from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=255)  # Event title
    description = models.TextField()  # Event details
    location = models.CharField(max_length=255)  # Where the event will be
    start_time = models.DateTimeField()  # When it starts
    end_time = models.DateTimeField()  # When it ends
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_events")  
    created_at = models.DateTimeField(auto_now_add=True)  # Auto set timestamp


class AdminNote(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)  # Admin who wrote the note

class EventReport(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField()
    resolved = models.BooleanField(default=False)
    reported_at = models.DateTimeField(auto_now_add=True)

class SystemLog(models.Model):
    action = models.CharField(max_length=255)
    performed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)


    def __str__(self):
        return f"Note for {self.event.title} by {self.admin.username}"

