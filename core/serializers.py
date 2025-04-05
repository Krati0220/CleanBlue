from rest_framework import serializers
from .models import CleanupEvent, Participation, YearlyImpact
from django.contrib.auth.models import User

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CleanupEvent
        fields = '__all__'

class ParticipationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participation
        fields = '__all__'

class YearlyImpactSerializer(serializers.ModelSerializer):
    class Meta:
        model = YearlyImpact
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
