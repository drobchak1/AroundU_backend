from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Visitors, Coorganizers #ImageofEvent, 
from users.models import User, ImageofUser
from .forms import EventForm
from .serializers import EventSerializer, VisitorsSerializer, UserSerializer     #, ImageofEventSerializer, ImageofUserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics,permissions
from django.contrib.auth.decorators import login_required
from .permissions import IsAuthorOrReadOnly
from rest_flex_fields.views import FlexFieldsModelViewSet

# class-based views
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

class OrganizerEventList(generics.ListCreateAPIView):
    # queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # queryset = Event.objects.all()
        # return queryset.filter(organizer_id=organizer_id)
        return Event.objects.filter(organizer=self.kwargs['organizer'])


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

class VisitorsList(generics.ListCreateAPIView):
    queryset = Visitors.objects.all()
    serializer_class = VisitorsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class VisitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visitors.objects.all()
    serializer_class = VisitorsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]   

# class ImageofEventViewSet(FlexFieldsModelViewSet):

#     serializer_class = ImageofEventSerializer
#     queryset = ImageofEvent.objects.all()

# class ImageofUserViewSet(FlexFieldsModelViewSet):

#     serializer_class = ImageofUserSerializer
#     queryset = ImageofUser.objects.all()

#     def perform_create(self, serializer):
#         serializer.save(organizer=self.request.user)

# function-based views

@api_view(['GET','POST'])
def events(request):
    if request.method == 'GET':
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EventSerializer(data=request.data, author=request.user)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def event_detail(request, pk):
    event = get_object_or_404(Event,pk=pk)
    if request.method == 'GET':
        serializer = EventSerializer(event)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@login_required
@api_view(['GET','POST', 'DELETE'])
def join_event(request, pk):
    user = request.user
    event = get_object_or_404(Event,pk=pk)
    if request.method == 'POST':
        serializer = VisitorsSerializer(user=user, event=event)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





def event_create_view(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = EventForm()

    context = {
        'form': form
    }
    return render (request, "events/create_event.html", context)

def dynamic_lookup_view(request,id):
    obj = get_object_or_404(Event,id=id)
    context = {
        'object': obj
    }
    return render (request, "events/event_detail.html", context)

def event_list_view(request):
    queryset = Event.objects.all()
    context = {
        "object_list": queryset
    }
    return render (request, "event_list.html", context)

