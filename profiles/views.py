from rest_framework import serializers
from .models import Profile
from django.views.generic import DetailView

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class ProfileDetailView(DetailView):
    model = Profile
    template_name = "profiles/profile_detail.html"  # Ensure this template exists
    context_object_name = "profile"