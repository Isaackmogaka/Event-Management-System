from django.urls import path
from .views import UserDetailView

urlpatterns = [
    path('user/', UserDetailView.as_view(), name='user-detail'),
]
