from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import CleanupEvent, Participation, YearlyImpact
from .serializers import EventSerializer, ParticipationSerializer, YearlyImpactSerializer
from django.contrib.auth.models import User
from .serializers import UserSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = CleanupEvent.objects.all()
    serializer_class = EventSerializer

class ParticipationViewSet(viewsets.ModelViewSet):
    queryset = Participation.objects.all()
    serializer_class = ParticipationSerializer

class YearlyImpactViewSet(viewsets.ModelViewSet):
    queryset = YearlyImpact.objects.all()
    serializer_class = YearlyImpactSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
