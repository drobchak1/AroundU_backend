from rest_framework import serializers
from .models import Event, Visitors, Coorganizers    #, ImageofEvent
from users.models import User   #, ImageofUser
from versatileimagefield.serializers import VersatileImageFieldSerializer

# class ImageofEventSerializer(serializers.ModelSerializer):
#     image = VersatileImageFieldSerializer(
#         sizes=[
#             ('full_size', 'url'),
#             ('thumbnail', 'thumbnail__100x100'),
#         ]
#     )

#     class Meta:
#         model = ImageofEvent
#         fields = ['pk', 'image']

# class ImageofUserSerializer(serializers.ModelSerializer):
#     image = VersatileImageFieldSerializer(
#         sizes=[
#             ('full_size', 'url'),
#             ('thumbnail', 'thumbnail__100x100'),
#         ]
#     )

#     class Meta:
#         model = ImageofUser
#         fields = ['pk', 'image']

class EventSerializer(serializers.ModelSerializer):
    # author = serializers.ReadOnlyField(source='author.username')
    visitors = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    coorganizers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    image = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
        ],
        allow_null=True
    )
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
    image = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
        ]
    )
    class Meta:
        model = User
        fields = '__all__'


