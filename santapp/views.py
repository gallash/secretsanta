import time # Used to create the username: username=str(round(time.time()))

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, EventForm


# Things I want to add:
# 1. A functionality in the backend able to notify by email and the users 
# dashboards when someone enters or leaves the room. When will the event take
# place. Updates on the event, if something is modified


# One of the only pages that do not require the user to be logged in
def landing_page(request):
    return render(request, template_name="santapp/landing-page.html", 
        context={})


def user_registration(request):
    # Only ever used when creating the User who will become the organizer
    if request.method=="POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # form.cleaned_data[] # Useful when I don't actually want to save 
            # the form, but extract data from it
            form.save()
            return redirect("landing-page") # The User can now select 
            # "CREATE A ROOM" again and be taken to the correct place 
            # "CREATE A ROOM" can be either on the page or in the navbar
    else:
        form = UserRegistrationForm()
    context={'form': form}
    return render(request, template_name="santapp/user-registration.html", 
        context=context)


@login_required
def event_creation(request):
    # Allows organizer to create an Event
    # It will also automatically create the Users and Participants accounts
    # And will ask Django to send emails to the participants afterwards
    #
    # It uses another function, fetching_data_ajax(), '#heling function',
    # that will run at the same as this very function, in order to make the
    # data from the frontend be sent via AJAX using jQuery, without the 
    # need to reload the page
    #
    # Here, the data is not saved from the Forms, but from the AJAX requisition

    if request.method == 'POST':
        pass

        # After saving the Event and Participants data to the database,
        # run the function that draws names, save the exchange list in the 
        # Event.exchange_list field and run the function to send emails
    else:
        form = EventForm()
    context = {'form': form}
    return render(request, template_name="santapp/event_creation.html", 
        context=context)


@login_required
def redirector(request, room_link):
    # Receives the link to the room and redirects the user to the intended room
    # Requires the Room model, possessing the link to it
    pass


# ---- Organizer and Attendees area
@login_required
def dashboard(request):
    # >>> ACCESSIBLE ONLY WHEN THE EVENT EXISTS
    # Here the user will see which users are participating, who has bought 
    # the gifts to be sent, information on the event, etc
    # The organizor will have a button to delete or update the Event
    pass


@login_required
def profile(request):
    # >>> ACCESSIBLE ONLY WHEN THE EVENT EXISTS
    # Simple profile to show a little of the user. He or she can write a short
    # description of his or hers (may show their personalities, hobbies, 
    # interests), as well as their wishlist and blacklist
    # Remember, the best gift may not even be something they know they want
    # 
    # The owner of the profile will be able to modify it
    # A visitor to that profile will not, obviously, be able to edit it
    pass





# ---- Helping functions
def fetching_data_ajax(request):
    pass

def user_participant_creation(request, is_organizer:bool):
    # Used inside the View related to creation of an Event 
    # (and subsequent creation of the Participant object for the organizer) and
    # for the creation of the User and Participant objects for each in the 
    # participants list
    
    if is_organizer is True:
        # Create Participant
        pass
    else:
        # Create User and Participant
        pass


def drawing_names(request) -> list:
    # Pulls all the IDs of all Participants in the Room
    # Shuffles the list of IDs. Gets the following, as an example
    # [id3, id0, id5, id2, id1, id4]
    # Makes the following connexion:
    # id3 receives from id4 and gifts id0
    # id0 receives from id3 and gifts id5
    # id5 receives from id0 and gifts id2
    # id2 receives from id5 and gifts id1
    # id1 receives from id2 and gifts id4
    # id4 receives from id1 and gifts id3


    # In the event of someone pulling out of the game:
    # [id3, id0, id2, id1, id4], id5 pulls out
    # id3 receives from id4 and gifts id0
    # id0 receives from id3 and gifts id2
    # id2 receives from id0 and gifts id1
    # id1 receives from id2 and gifts id4
    # id4 receives from id1 and gifts id3
    #
    # Before saving in the database, ask the id0 if it is OK for him/her 
    # that the new gifted is id2
    pass