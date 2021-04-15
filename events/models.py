from django.db import models
# from users.models import AppUser 
from django.contrib.auth.models import User

# Create your models here.
# def get_image_path(instance, filename):
#     return os.path.join('photos', str(instance.id), filename)

# class User(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)

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
    # image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    date_and_time_of_event = models.DateTimeField()
    max_number_of_people = models.IntegerField(null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    visitors_count = models.IntegerField(default=0)
    organizer = models.ForeignKey('auth.User', related_name='events', on_delete=models.CASCADE) #if author is deleted - events are deleted 
        
    def get_absolute_url(self):
        return f"/events/{self.id}/"

    class Meta:
        ordering = ['date_of_creation']

class Visitors(models.Model):
    user=models.ForeignKey('auth.User', related_name='visitors', on_delete=models.CASCADE)
    event=models.ForeignKey('Event', related_name='visitors',on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "event")

class Coorganizers(models.Model):
    user=models.ForeignKey('auth.User', related_name='visitors', on_delete=models.CASCADE)
    event=models.ForeignKey('Event', related_name='visitors',on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "event")