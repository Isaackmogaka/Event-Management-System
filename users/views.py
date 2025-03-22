# # from django.shortcuts import render
# # from rest_framework.response import Response
# # from rest_framework.views import APIView
# # from rest_framework.permissions import AllowAny, IsAuthenticated
# # from rest_framework_simplejwt.tokens import RefreshToken
# # from django.contrib.auth.models import User
# # from django.contrib.auth import authenticate
# # from rest_framework import status
# # from users.serializers import UserSerializer
# # from django.contrib.auth.models import User
# # from rest_framework import generics
# # from rest_framework.permissions import AllowAny, IsAuthenticated
# # from .models import Profile
# # from .serializers import RegisterSerializer, ProfileSerializer
# # from rest_framework import generics, permissions
# # from .models import Event, Review
# # from .serializers import EventSerializer, ReviewSerializer

# # # Register a new user
# # class RegisterView(APIView):
# #     permission_classes = [AllowAny]

# #     def post(self, request):
# #         serializer = UserSerializer(data=request.data)
# #         if serializer.is_valid():
# #             user = serializer.save()
# #             return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # # Login and get token
# # class LoginView(APIView):
# #     permission_classes = [AllowAny]

# #     def post(self, request):
# #         username = request.data.get("username")
# #         password = request.data.get("password")
# #         user = authenticate(username=username, password=password)

# #         if user:
# #             refresh = RefreshToken.for_user(user)
# #             return Response({
# #                 "refresh": str(refresh),
# #                 "access": str(refresh.access_token)
# #             })
# #         return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

# # # Logout (JWT doesn't have a direct logout, but we can invalidate the token manually)
# # class LogoutView(APIView):
# #     permission_classes = [IsAuthenticated]

# #     def post(self, request):
# #         try:
# #             refresh_token = request.data["refresh"]
# #             token = RefreshToken(refresh_token)
# #             token.blacklist()
# #             return Response({"message": "Successfully logged out"}, status=status.HTTP_205_RESET_CONTENT)
# #         except Exception:
# #             return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)

# # # Get authenticated user details
# # class UserDetailView(APIView):
# #     permission_classes = [IsAuthenticated]

# #     def get(self, request):
# #         serializer = UserSerializer(request.user)
# #         return Response(serializer.data)
    
# # class RegisterView(generics.CreateAPIView):
# #     queryset = User.objects.all()
# #     serializer_class = RegisterSerializer
# #     permission_classes = [AllowAny]

# # class ProfileView(generics.RetrieveUpdateAPIView):
# #     queryset = Profile.objects.all()
# #     serializer_class = ProfileSerializer
# #     permission_classes = [IsAuthenticated]

# #     def get_object(self):
# #         return self.request.user.profile

# # class EventListCreateView(generics.ListCreateAPIView):
# #     queryset = Event.objects.all()
# #     serializer_class = EventSerializer
# #     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# #     def perform_create(self, serializer):
# #         serializer.save(created_by=self.request.user)

# # class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
# #     queryset = Event.objects.all()
# #     serializer_class = EventSerializer
# #     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# # class ReviewListCreateView(generics.ListCreateAPIView):
# #     queryset = Review.objects.all()
# #     serializer_class = ReviewSerializer
# #     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# #     def perform_create(self, serializer):
# #         serializer.save(user=self.request.user)
# # # Create your views here.


# from django.contrib.auth.models import User
# from rest_framework import generics, status
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework_simplejwt.tokens import RefreshToken
# from .models import Profile
# from .serializers import UserSerializer, ProfileSerializer, CustomTokenObtainPairSerializer

# # ✅ User Registration
# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]

#     def create(self, request, *args, **kwargs):
#         response = super().create(request, *args, **kwargs)
#         user = User.objects.get(username=request.data['username'])
#         return Response({
#             "message": "User registered successfully",
#             "user": UserSerializer(user).data
#         }, status=status.HTTP_201_CREATED)


# # ✅ User Login (JWT)
# class LoginView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer


# # ✅ User Logout (Blacklisting Token)
# class LogoutView(generics.GenericAPIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         try:
#             refresh_token = request.data["refresh"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#             return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)


# # ✅ User Profile (Retrieve & Update)
# class ProfileView(generics.RetrieveUpdateAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [IsAuthenticated]

#     def get_object(self):
#         return self.request.user.profile  # Get the profile of the authenticated user
# views.py
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Profile
from .serializers import UserSerializer, ProfileSerializer, CustomTokenObtainPairSerializer

# ✅ User Registration
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=request.data['username'])
        return Response({
            "message": "User registered successfully",
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name
            }
        }, status=status.HTTP_201_CREATED)


# ✅ User Profile (Retrieve & Update)
class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile  # Get the profile of the authenticated user

# ✅ Login View (Using Custom JWT Serializer)
class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


# ✅ Logout View: Blacklist Refresh Token on Logout
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()  # ✅ Blacklist the token to prevent reuse
            return Response({"detail": "Successfully logged out."}, status=200)
        except Exception as e:
            return Response({"error": "Invalid token or request."}, status=400)

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name
        })