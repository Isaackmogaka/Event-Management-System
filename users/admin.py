from django.contrib import admin

# from .models import Profile
from .models import Attendance
from .models import EventComment
from .models import EventReview
# from .models import Notification

# Register your models here.

# admin.site.register(Profile)
admin.site.register(Attendance)
admin.site.register(EventComment)
admin.site.register(EventReview)
# admin.site.register(Notification)
