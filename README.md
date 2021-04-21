# AroundU_backend

http://127.0.0.1:8000/admin/ - доступ до адміністрації django  
http://127.0.0.1:8000/events/ - GET - дозволяє отримати JSON-список івентів  
http://127.0.0.1:8000/events/ - POST - дозволяє створити новий івент  
http://127.0.0.1:8000/events/<int:pk>/ - перегляд окремого JSON-івента через GET. Для автора - оновлення через PUT і видалення через DELETE  
http://127.0.0.1:8000/users/ - список юзерів в JSON.  
http://127.0.0.1:8000/users/<int:pk>/ - перегляд окремого юзера в JSON  
http://127.0.0.1:8000/visitors/ - перегляд всіх "відвідувань" в JSON  

## Модель івента  
```
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
    # cover = models.ImageField(upload_to=get_image_path, blank=True, null=True)  
    max_number_of_people = models.IntegerField(null=True,blank=True)  
    price = models.IntegerField(null=True,blank=True)  
    organizer = models.CharField(max_length=150)  
    date_of_creation = models.DateTimeField(auto_now_add=True)  
    author = models.ForeignKey('auth.User', related_name='events', on_delete=models.CASCADE) #if author is deleted - events are deleted  
    visitors_count = models.IntegerField(default=0)  
```
## Модель відвідування    

```
class Visitors(models.Model):  
    user=models.ForeignKey('auth.User', related_name='visitors', on_delete=models.CASCADE)  
    event=models.ForeignKey('Event', related_name='visitors',on_delete=models.CASCADE)  
```

## Дані адміна 

Логін: useradmin  
Пароль: lol1lol1  
