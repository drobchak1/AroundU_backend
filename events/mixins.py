from rest_framework.decorators import action
from rest_framework.response import Response

from events import services
from users.serializers import UserSerializer


class VisitMixin:
    @action(detail=True, methods=['post'])
    def visit(self, request, pk=None):
        """Visit event.
        """
        obj = self.get_object()
        services.add_visit(obj, request.user)
        return Response()


    @action(detail=True, methods=['post'])
    def unvisit(self, request, pk=None):
        """Unvisit event.
        """
        obj = self.get_object()
        services.remove_visit(obj, request.user)
        return Response()
        

    @action(detail=True, methods=['get'])
    def visitors(self, request, pk=None):
        """Get all people, who visit event.
        """
        obj = self.get_object()
        fans = services.get_visitors(obj)
        serializer = UserSerializer(fans, many=True)
        return Response(serializer.data)