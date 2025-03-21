from django.urls import path
from .views import EventListCreateView, EventDetailView, ReviewListCreateView
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def home_view(request):
    return HttpResponse("<h1>Welcome to the Event Management System API</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),  
    path('api/events/', include('events.urls')),
    path('', home_view),  # This adds a default homepage
]
urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
]


