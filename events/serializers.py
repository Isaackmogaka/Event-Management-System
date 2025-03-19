from rest_framework import serializers
from .models import Event, Review  # Import Event and Review models

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'  # Ensure all required fields are included

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'  # Include all fields for reviews
