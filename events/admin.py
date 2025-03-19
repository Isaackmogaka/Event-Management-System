from django.contrib import admin

from .models import Event  # Import your model
from .models import AdminNote
from .models import EventReport
from .models import SystemLog
from .models import Category

# Register your models here.
admin.site.register(Event)  # Register the model
admin.site.register(AdminNote)
admin.site.register(EventReport)
admin.site.register(SystemLog)
admin.site.register(Category)


