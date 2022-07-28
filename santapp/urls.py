from django.urls import path
from . import views


urlpatterns = [
    path("registration/", views.user_registration, name="user-registration"),
    path("dashboard/", views.dashboard, name="event-dashboard"),
    path('event-creation/', views.event_creation, name="event-creation"),
    path("", views.landing_page, name="landing-page"),
]