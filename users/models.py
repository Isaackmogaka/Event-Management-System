from django.db import models
from django.contrib.auth.models import User
from events.models import Event


# Create your models here.
class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey("events.Event", on_delete=models.CASCADE)  # FIXED: Correct reference
    status = models.CharField(
        max_length=10,
        choices=[('Going', 'Going'), ('Interested', 'Interested'), ('Not Going', 'Not Going')],
        default='Interested'
    )
    timestamp = models.DateTimeField(auto_now_add=True)

class EventComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey("events.Event", on_delete=models.CASCADE)  # FIXED: Correct reference
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class EventReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey("events.Event", on_delete=models.CASCADE)  # FIXED: Correct reference
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # 1-5 stars
    review = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone_number = models.CharField(max_length=15, blank=True, null=True)
#     profile_pic = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
#     bio = models.TextField(blank=True, null=True)
#     is_organizer = models.BooleanField(default=False)  # Whether the user can create events


# class Attendance(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     event = models.ForeignKey('Event', on_delete=models.CASCADE)
#     status = models.CharField(
#         max_length=10,
#         choices=[('Going', 'Going'), ('Interested', 'Interested'), ('Not Going', 'Not Going')],
#         default='Interested'
#     )
#     timestamp = models.DateTimeField(auto_now_add=True)

# class EventComment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     event = models.ForeignKey('Event', on_delete=models.CASCADE)
#     comment = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

# class EventReview(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     event = models.ForeignKey('Event', on_delete=models.CASCADE)
#     rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # 1-5 stars
#     review = models.TextField(blank=True, null=True)
#     timestamp = models.DateTimeField(auto_now_add=True)

# class Notification(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     message = models.TextField()
#     is_read = models.BooleanField(default=False)
#     timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username} - {self.event.title} ({self.status})"
