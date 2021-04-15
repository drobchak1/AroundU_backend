from rest_framework import serializers
from .models import Event, Visitors, Coorganizers
from users.models import User

class EventSerializer(serializers.ModelSerializer):
    # author = serializers.ReadOnlyField(source='author.username')
    visitors = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Event
        fields = '__all__'

class VisitorsSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Visitors
        fields = '__all__'

class CoorganizersSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Coorganizers
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    events = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    visitors = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = '__all__'