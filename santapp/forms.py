from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Event, Participant


class UserRegistrationForm(UserCreationForm):
    # I will make 'username' invisible to the User
    # And I will fill the data using jQuery. I will get the string before
    # '@' in the email and use that as the username
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 
            'password1', 'password2']


class EventForm(forms.ModelForm):
    # The init function aims to making the listed fields required
    organizer = User


    class Meta:
        model = Event
        fields = ['event_name', 'is_remote', 'place', 'online_meeting_link',
            'rules', 'price_range']


class ParticipantForm(Participant):
    pass