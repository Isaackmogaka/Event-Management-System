# from django.shortcuts import render
# from rest_framework import serializers
# from events.serializers import ReviewSerializer
# from .models import Review

# # Create your views here.
# from rest_framework import generics
# from .models import Event
# from .serializers import EventSerializer
# from rest_framework.permissions import IsAuthenticatedOrReadOnly

# class EventListCreateView(generics.ListCreateAPIView):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]  # Only logged-in users can create events

# class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]  # Only authenticated users can edit/delete

# class ReviewListCreateView(generics.ListCreateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer 
# 
from rest_framework import generics
from .models import Event, Review  # Import the models
from .serializers import EventSerializer, ReviewSerializer  # Ensure this matches your serializers file

class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

