"""AroundU URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from events.views import event_create_view, event_list_view, dynamic_lookup_view, events, event_detail, join_event, UserList, UserDetail, EventList, EventDetail, VisitorsList, VisitDetail, OrganizerEventList, ImageofEventViewSet, ImageofUserViewSet
from users.views import signup
# Images
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'image_of_event', ImageofEventViewSet, basename='ImageofEvent')
router.register(r'image_of_user', ImageofUserViewSet, basename='ImageofUser')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events_old/create/', event_create_view),
    path('events_old/<int:id>/', dynamic_lookup_view),
    path('events_old/', event_list_view),
    path('signup/', signup),
    # Combining the views with these URL patterns creates the get posts/, post posts/, get posts/<int:pk>/, put posts/<int:pk>/, and delete posts/<int:pk>/ endpoints
    path('events/', EventList.as_view()),
    path('events/<int:pk>/', EventDetail.as_view()),
    # path('image_of_event/<int:pk>/', ImageofEventViewSet.as_view()),
    # path('events/', events),
    # path('events/<int:id>/', event_detail),
    path('events/<int:id>/join', join_event),
    path('users/', UserList.as_view()),
    path('users/<int:organizer>/events', OrganizerEventList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('visitors/', VisitorsList.as_view()),
    path('visitors/<int:pk>/', VisitDetail.as_view()),
    # Log_in button
    path('api-auth/', include('rest_framework.urls')),
    url(r'^', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)