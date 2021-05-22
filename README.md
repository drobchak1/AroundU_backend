# AroundU_backend
  
Через браузер в Джанго є функція перегляду json-запитів через браузер. Запити можна додавати через HTML-form, або Raw data (JSON-файл)  
  
**/admin/** - доступ до адміністрації django  
**/events/** - GET - дозволяє отримати JSON-список івентів  
**/events/** - POST - дозволяє створити новий івент  
**/events/**<int:pk>/ - перегляд окремого JSON-івента через GET. Для автора - оновлення через PUT і видалення через DELETE  
**/users/** - список юзерів в JSON.  
**/users/<int:pk>/** - перегляд окремого юзера в JSON  
**/users/<int:organizer>/events** - всі івенти створені одним організатором  
**/visitors/** - перегляд всіх "відвідувань" в JSON, POST дозволяє юзеру додатись в потрібний івент  
**/visitors/<int:pk>/** - перегляд окремого "відвідування", можливість видалити його (для юзера, який відвідує)  
**/register/** - реєстрація в POST-запиті  
**/api-token-auth/** - авторизація через токен  
**/change_password/<int:pk>/** - зміна пароля для юзера з відповідним id (POST)  
**/update_profile/<int:pk>/** - оновлення профіля для юзера з відповідним id (POST)  
  
## Важливо  
На heroku не працюють, на жаль, зображення. Щоб вони працювали - потрібно інтегрувати Amazon.  
Додавати зображення в юзерів та івенти НЕ МОЖНА, це зіпсує роботу сторінок /events/, /users/.  
В офлайн же версії (при скачуванні і запуску локально) зображення працюють.  
  
## Дані адміна та юзерів  
  
Логін: admin  
Пароль: lol1lol1  
  
Юзерів додаткових двоє - user1 і user2. Обидва мають пароль lol1lol1  
Ви можете зробити скільки завгодно юзерів через шлях /register/ або через сторінку /admin/users/user/  
  
## Модель івента  
Обов'язкові поля title, description, event_type, city, address, date_and_time_of_event. Інші опціональні  
```
title = models.CharField(max_length=120)  
description = models.TextField()  
EVENT_TYPE = (  
    ('PRI', 'Private event'),  
    ('PUB', 'Public event'),  
    ('ONL', 'Online event'),  
)  
event_type = models.CharField(max_length=3,choices=EVENT_TYPE)  
city = models.CharField(max_length=50)  
address = models.CharField(max_length=100)  
# image = models.ImageField(upload_to=get_image_path, blank=True, null=True)  
date_and_time_of_event = models.DateTimeField()  
max_number_of_people = models.IntegerField(null=True,blank=True)  
price = models.IntegerField(null=True,blank=True)  
date_of_creation = models.DateTimeField(auto_now_add=True)  
visitors_count = models.IntegerField(default=0)  
organizer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='events', on_delete=models.CASCADE)  
# image = models.ForeignKey('ImageofEvent', related_name='events', blank=True,null=True, on_delete=models.CASCADE)  
image = VersatileImageField(
    #'ImageofEvent',
    upload_to='images/',
    ppoi_field='image_ppoi', 
    blank=True,
    null=True,
)  
image_ppoi = PPOIField()  
```
## Модель відвідування    
  
```
class Visitors(models.Model):  
    user=models.ForeignKey('auth.User', related_name='visitors', on_delete=models.CASCADE)  
    event=models.ForeignKey('Event', related_name='visitors',on_delete=models.CASCADE)  
```
  
## Модель юзера    
Обов'язкові для реєстрації username, password, email. Інші опціональні
  
```
    username =  
    password =  
    email =  
    first_name = models.CharField('first name', max_length=30, null=True, blank=True)
    last_name = models.CharField('last name', max_length=150, null=True, blank=True)
    bio = models.TextField(null=True,blank=True)
    city = models.CharField(max_length=20,null=True,blank=True)
    phone = models.CharField(max_length=20,null=True,blank=True)
    image = VersatileImageField(
        upload_to='images/',
        ppoi_field='image_ppoi', 
        blank=True,
        null=True,
)  
```
  
