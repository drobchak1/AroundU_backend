# AroundU_backend

Через браузер в Джанго є функція перегляду json-запитів через браузер. Запити можна додавати через HTML-form, або Raw data (JSON-файл)
/admin/ - доступ до адміністрації django  
/events/ - GET - дозволяє отримати JSON-список івентів  
/events/ - POST - дозволяє створити новий івент  
/events/<int:pk>/ - перегляд окремого JSON-івента через GET. Для автора - оновлення через PUT і видалення через DELETE  
/users/ - список юзерів в JSON.  
/users/<int:pk>/ - перегляд окремого юзера в JSON  
/visitors/ - перегляд всіх "відвідувань" в JSON, POST дозволяє юзеру додатись в потрібний івент

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

Логін: admin  
Пароль: lol1lol1  
