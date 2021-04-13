from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    # title = forms.CharField(label='Title',
    #     widget=forms.TextInput(attrs={"placeholder": "Title of your event"}))
    # # event_type=forms.ChoiceField()
    # description = forms.CharField(
    #     widget=forms.Textarea(
    #         attrs={"placeholder": "Description of your event",}))
    # city = forms.CharField(label='City',
    #     widget=forms.TextInput(attrs={"placeholder": "City where your event will be held"})) 
    # address = forms.CharField(label='Address',
    #     widget=forms.TextInput(attrs={"placeholder": "Address where your event will be held"})) 
    # price = forms.DecimalField()
    # organizer = forms.CharField(label='Organizer',
    #     widget=forms.TextInput(attrs={"placeholder": "Leave it blank if you are the organizer"})) 
    class Meta:
        model = Event
        fields = [
            'title',
            'event_type',
            'description',
            'city',
            'address',
            'date_and_time_of_event',
            'max_number_of_people',
            'price',
            'organizer',
        ]