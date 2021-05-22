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
from events.views import event_create_view, event_list_view, dynamic_lookup_view, events, event_detail, join_event, EventList, EventDetail, VisitorsList, VisitDetail, OrganizerEventList   #, ImageofEventViewSet, ImageofUserViewSet
from users.views import signup, MyObtainTokenPairView, RegisterView, ChangePasswordView, UpdateProfileView, UserList, UserDetail
# Images
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.authtoken.views import obtain_auth_token

# router = DefaultRouter()
# router.register(r'image_of_event', ImageofEventViewSet, basename='ImageofEvent')
# router.register(r'image_of_user', ImageofUserViewSet, basename='ImageofUser')

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
    # path('events/<int:pk>/join', join_event),
    path('users/', UserList.as_view()),
    path('users/<int:organizer>/events', OrganizerEventList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('visitors/', VisitorsList.as_view()),
    path('visitors/<int:pk>/', VisitDetail.as_view()),
    # Login and logout
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    # url(r'^', include(router.urls)),
    ###################LOGIN NEEDS WORK
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)