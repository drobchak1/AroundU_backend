from django.db import models
from users.models import User 
from AroundU import settings
from versatileimagefield.fields import VersatileImageField, PPOIField
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# from django.contrib.auth.models import User

class Visitors(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='visitors',
                             on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    date_of_creation = models.DateTimeField(auto_now_add=True)


class Event(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    EVENT_TYPE = (
        ('PRI', 'Private event'),
        ('PUB', 'Public event'),
        ('ONL', 'Online event'),
    )
    event_type = models.CharField(max_length=3, choices=EVENT_TYPE)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    date_and_time_of_event = models.DateTimeField()
    max_number_of_people = models.IntegerField(null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='events', on_delete=models.CASCADE)
    image = VersatileImageField(
        #'ImageofEvent',
        upload_to='images/',
        ppoi_field='image_ppoi', 
        blank=True,
        null=True,
    )
    image_ppoi = PPOIField()
    visitors = GenericRelation(Visitors)
    date_of_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def total_visitors(self):
        return self.likes.count()
        
    def get_absolute_url(self):
        return f"/events/{self.id}/"

    class Meta:
        ordering = ['date_of_creation']



# class Visitors(models.Model):
#     user=models.ForeignKey(settings.AUTH_USER_MODEL, related_name='visitors', on_delete=models.CASCADE)
#     event=models.ForeignKey('Event', related_name='visitors',on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ("user", "event")

# class Coorganizers(models.Model):
#     user=models.ForeignKey(settings.AUTH_USER_MODEL, related_name='coorganizers', on_delete=models.CASCADE)
#     event=models.ForeignKey('Event', related_name='coorganizers',on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ("user", "event")

# class ImageofEvent(models.Model):
#     # name = models.CharField(max_length=255)
#     image = VersatileImageField(
#         'ImageofEvent',
#         upload_to='images/',
#         ppoi_field='image_ppoi'
#     )
#     image_ppoi = PPOIField()

#     def __str__(self):
#         return self.name