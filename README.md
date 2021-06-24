# AroundU_backend
  
Через браузер в Джанго є функція перегляду json-запитів через браузер. Запити можна додавати через HTML-form, або Raw data (JSON-файл)  
  
**/admin/** - django administration  
**/events/** - events-list (GET) and event-creation(POST)  
**/events/**<int:pk>/ - перегляд окремого JSON-івента через GET. Для автора - оновлення через PUT і видалення через DELETE  
**/events/<int:pk>/visit/** - Visit event  
**/events/<int:pk>/unvisit/** - Unvisit event  
**/events/<int:pk>/visitors/** - List of users who visit event  
**/users/** - список юзерів в JSON.  
**/users/<int:pk>/** - перегляд окремого юзера в JSON  
**/users/<int:organizer>/events** - всі івенти створені одним організатором  
**/visitors/** - перегляд всіх "відвідувань" в JSON, POST дозволяє юзеру додатись в потрібний івент  
**/visitors/<int:pk>/** - перегляд окремого "відвідування", можливість видалити його (для юзера, який відвідує)  
**/register/** - реєстрація в POST-запиті  
**/api-token-auth/** - авторизація через токен  
**/change_password/<int:pk>/** - зміна пароля для юзера з відповідним id (POST)  
**/update_profile/<int:pk>/** - оновлення профіля для юзера з відповідним id (POST)  
**/token/** - JWT token acquiring  
**/token/refresh/** - JWT token refresh  
  
  
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
  
