
from django.urls import path
from .views import EventListView, EventDetailView, register_for_event

urlpatterns = [
    path("", EventListView.as_view(), name="event_list"),
    path("<int:pk>/", EventDetailView.as_view(), name="event_detail"),
    path("<int:pk>/register/", register_for_event, name="event_register"),
]
