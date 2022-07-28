import datetime

from django.db import models
from django.contrib.auth.models import User


## Construction of this system
# Remember, so far the idea is to make the new Participant receive emails from
# the backend of the site and also be able to come to the platform and alter 
# some information (address, wishlist, blacklist, description) all of which are
# optional
#
# Form (create Room):
#   Create Event
#   List of info about users -> create 
# Send email
# Pages



class Event(models.Model):
    # Receive many participants per Event, including the organizer, 
    # automatically, but only one organizer
    organizer = models.ForeignKey(User, on_delete=models.PROTECT, default=None)
    event_name = models.CharField(max_length=32, default=None, null=True, 
        blank=True)
    
    is_remote = models.BooleanField(default=False)
    place = models.CharField(max_length=2048, default=None, 
        null=True, blank=True)
    online_meeting_link = models.CharField(max_length=128, default=None, 
        null=True, blank=True)
    rules = models.TextField(default=None, null=True, blank=True)
    price_range = models.FloatField(default=0.00, null=True, blank=True)
    # date = models.DateField() # How to implement the verifier:
    # if date is before today: forbid
    # if date is within 14 days (2 weeks): alert the organizer of the time
    # if date is above 2 years: forbid (avoid cluttering the database)

    # Storing the resulting list of the 'drawing_names' function
    exchange_list = models.CharField(max_length=2048, default=None, 
        null=True, blank=True)

    # Good for helping the function that draws names
    def comma_separated_exchange_list(self):
        lst = [int(ID) for ID in str(self.exchange_list).split()]
        return lst

    # def get_participants(self):
    #     return Event.objects.get(pk=self.pk).participant_set.all()

    def __str__(self):
        return self.event_name


# class Participant(User):
class Participant(models.Model):
    # According to Django's own documentation, by extending the User model
    # through the use of OneToOneField, we can annex additional information
    # to the User, without dealing with authorization. Check the page for 
    # further information on how to make this happen:
    # https://docs.djangoproject.com/en/4.0/topics/auth/customizing/
    # 
    # Basically I create the user and then I can add info to it?
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None,
        null=True, blank=True)

    is_organizer = models.BooleanField(default=False) # Change to True when
    # he/she clicks to create a room
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default=None)

    # Info of the user
    email = models.EmailField(max_length=255, default=None) # unique=True later
    first_name = models.CharField(max_length=32, default=None)
    last_name = models.CharField(max_length=32, default=None)
    nickname = models.CharField(max_length=32, default=None, 
        null=True, blank=True) 
    # Useful to distinguish between
    # two people with the same name. OR the JS (jQuery?) will take care of 
    # observing if two people have the same name, in which case it asks for a 
    # nickname

    # Extra info of the user
    # Things they love (e.g., games, wine, romantic books)
    wishlist = models.CharField(max_length=2048, default=None, 
        null=True, blank=True)
    blacklist = models.CharField(max_length=2048, default=None, 
        null=True, blank=True)
    description_of_yourself = models.TextField(max_length=2048, default=None, 
        null=True, blank=True)
    address = models.CharField(max_length=2048, default=None, 
        null=True, blank=True)

    gives_to = models.IntegerField(default=None, null=True, blank=True)
    receives_from = models.IntegerField(default=None, null=True, blank=True)
    password = models.CharField(max_length=64, default=None,
        null=True, blank=True)

    # A marker to show If he/she has bought the gifts
    has_bought = models.BooleanField(default=False, null=True, blank=True)

    # def create_participant_password(self):
    #     gifted = Participant.objects.get(pk=self.gives_to)
    #     return gifted.first_name + gifted.last_name

    def __str__(self):
        if self.nickname is None:
            str_ = f"{self.first_name} {self.last_name}"
        else:
            str_ = f"{self.first_name} ({self.nickname}) {self.last_name}"
        return str_


# class GiveReceiverTable(models.Model):
#     # This is a table detailing who will give and receive (all using IDs)
#     # 
#     pass

# makemigrations and migrate the database in the terminal to make the changes
# take effect