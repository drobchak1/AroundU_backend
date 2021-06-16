from rest_framework import serializers
from .models import Event, Visitors
# from users.models import User   #, ImageofUser
from versatileimagefield.serializers import VersatileImageFieldSerializer 
from events import services

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
    is_fan = serializers.SerializerMethodField()
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
            "organizer",
            # "visitors_count": null,
            # "organizer": null
            "visitors",
            "is_fan",
            "total_visitors",
        ]
        extra_kwargs = {
            "image": {"required": False},
            # "max_number_of_people": null,
            "price": {"required": False},
            # "visitors_count": null,
            # "organizer": null
            "visitors": {"required": False},
            "likes": {"required": False},
            "organizer": {"read_only": True},
            "total_likes": {"read_only": True},
            "is_fan": {"read_only": True},
        }
    def get_is_fan(self, obj) -> bool:
        user = self.context.get('request').user
        return services.is_fan(obj, user)

class VisitorsSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Visitors
        fields = '__all__'
