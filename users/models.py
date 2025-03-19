# from django.db import models
# from django.contrib.auth.models import User
# from events.models import Event

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(blank=True, null=True)
#     profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)


# # Create your models here.
# class Event(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     date = models.DateTimeField()
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE)

# class Attendance(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     event = models.ForeignKey("events.Event", on_delete=models.CASCADE)  # FIXED: Correct reference
#     status = models.CharField(
#         max_length=10,
#         choices=[('Going', 'Going'), ('Interested', 'Interested'), ('Not Going', 'Not Going')],
#         default='Interested'
#     )
#     timestamp = models.DateTimeField(auto_now_add=True)

# class EventComment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     event = models.ForeignKey("events.Event", on_delete=models.CASCADE)  # FIXED: Correct reference
#     comment = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

# class Review(models.Model):
#     event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="reviews")
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     comment = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)


#     def __str__(self):
#         return f"{self.user.username} - {self.event.title} ({self.status})"
from django.db import models
from django.contrib.auth.models import User
from events.models import Event  # ✅ Correct import for Event

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username  # ✅ Added __str__ for readability

class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)  # ✅ Direct reference to Event
    status = models.CharField(
        max_length=10,
        choices=[('Going', 'Going'), ('Interested', 'Interested'), ('Not Going', 'Not Going')],
        default='Interested'
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.event.title} ({self.status})"

class EventComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)  # ✅ Direct reference to Event
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} on {self.event.title}: {self.comment[:30]}..."  # ✅ Improved readability

class Review(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="user_reviews")  # Changed related_name
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_reviews")  # Changed related_name
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"  # ✅ Removed `status` (it doesn't exist)
   