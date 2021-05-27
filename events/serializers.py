from rest_framework import serializers
from .models import Event, Visitors, Coorganizers    #, ImageofEvent
# from users.models import User   #, ImageofUser
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
        allow_null=True,
        required=False
    )
    class Meta:
        model = Event
        fields = [
            "id",
            "image",
            "title",
            "description",
            "event_type",
            "city",
            "address",
            "date_and_time_of_event",
            # "max_number_of_people",
            "price",
            # "visitors_count": null,
            # "organizer": null
            "visitors",
            "coorganizers",
        ]
        extra_kwargs = {
            "image": {"required": False},
            # "max_number_of_people": null,
            "price": {"required": False},
            # "visitors_count": null,
            # "organizer": null
            "visitors": {"required": False},
            "coorganizers": {"required": False},
        }

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