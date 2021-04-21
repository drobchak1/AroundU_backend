from django.contrib import admin
from .models import Event, Visitors, Coorganizers, ImageofEvent

# Register your models here.
admin.site.register(Event)
admin.site.register(Visitors)
admin.site.register(Coorganizers)
admin.site.register(ImageofEvent)