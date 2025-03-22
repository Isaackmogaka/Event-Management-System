# from django.urls import path
# from .views import RegisterView, LoginView, LogoutView, UserDetailView, ProfileView

# urlpatterns = [
#     path('auth/register/', RegisterView.as_view(), name='register'),
#     path('auth/login/', LoginView.as_view(), name='login'),
#     path('auth/logout/', LogoutView.as_view(), name='logout'),
#     path('auth/user/', UserDetailView.as_view(), name='user-detail'),
#     path('profile/', ProfileView.as_view(), name='profile'),
# ]

from django.urls import path
from .views import RegisterView, LoginView, LogoutView, UserDetailView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/', UserDetailView.as_view(), name='user-detail'),
    path('profile/', ProfileView.as_view(), name='profile'),
]


