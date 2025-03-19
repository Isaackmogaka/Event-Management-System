from django.urls import path
from .views import EventListCreateView, EventDetailView
from django.urls import path, include  # Make sure 'include' is imported


urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
]
urlpatterns = [
    path('api/', include('events.urls')),  # Now, all event endpoints start with /api/
]