from django.urls import path
from .views import ProfileDetailView

urlpatterns = [
    path("me/", ProfileDetailView.as_view(), name="profile-detail"),
]


urlpatterns = [
    path("<int:pk>/", ProfileDetailView.as_view(), name="profile-detail"),
]