from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics,permissions
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets

from events.mixins import VisitMixin
from .serializers import EventSerializer, VisitorsSerializer
from users.serializers import UserSerializer
from .models import Event, Visitors
from users.models import User 
from .permissions import IsAuthorOrReadOnly, IsAuthorOrReadOnlyVisit


class EventViewSet(VisitMixin, viewsets.ModelViewSet):
    """CRUD operations on events and visits
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

# class-based views

# class EventList(generics.ListCreateAPIView):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(organizer=self.request.user)


class OrganizerEventList(generics.ListCreateAPIView):
    # queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # queryset = Event.objects.all()
        # return queryset.filter(organizer_id=organizer_id)
        return Event.objects.filter(organizer=self.kwargs['organizer'])

# class EventDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]


class VisitorsList(generics.ListCreateAPIView):
    queryset = Visitors.objects.all()
    serializer_class = VisitorsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class VisitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visitors.objects.all()
    serializer_class = VisitorsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnlyVisit]   