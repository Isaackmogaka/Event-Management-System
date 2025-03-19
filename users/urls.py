# from django.urls import path
# from users.views import RegisterView, LoginView, LogoutView, UserDetailView
# from django.urls import path, include
# from .views import RegisterView, ProfileView
# from django.urls import path
# from .views import EventListCreateView, EventDetailView, ReviewListCreateView

# urlpatterns = [
#     path('auth/register/', RegisterView.as_view(), name='register'),
#     path('auth/login/', LoginView.as_view(), name='login'),
#     path('auth/logout/', LogoutView.as_view(), name='logout'),
#     path('auth/user/', UserDetailView.as_view(), name='user-detail'),
# ]

# urlpatterns = [
#     path('api/', include('users.urls')),  # Include authentication endpoints
# ]

# urlpatterns = [
#     path('register/', RegisterView.as_view(), name='register'),
#     path('profile/', ProfileView.as_view(), name='profile'),
# ]

# urlpatterns = [
#     path('events/', EventListCreateView.as_view(), name='event-list-create'),
#     path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
#     path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
# ]

# from django.urls import path, include
# from users.views import RegisterView, LoginView, LogoutView, UserDetailView, ProfileView
# from events.views import EventListCreateView, EventDetailView, ReviewListCreateView

# urlpatterns = [
#     # Authentication Routes
#     path('auth/register/', RegisterView.as_view(), name='register'),
#     path('auth/login/', LoginView.as_view(), name='login'),
#     path('auth/logout/', LogoutView.as_view(), name='logout'),
#     path('auth/user/', UserDetailView.as_view(), name='user-detail'),
    
#     # User Profile
#     path('profile/', ProfileView.as_view(), name='profile'),

#     # Event Management
#     path('events/', EventListCreateView.as_view(), name='event-list-create'),
#     path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
#     path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
# ]
from django.urls import path
from .views import RegisterView, LoginView, LogoutView, UserDetailView, ProfileView

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('auth/user/', UserDetailView.as_view(), name='user-detail'),
    path('profile/', ProfileView.as_view(), name='profile'),
]

