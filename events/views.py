from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import Event
from .forms import EventRegistrationForm
from .models import Event, EventRegistration
from django.utils import timezone

class EventListView(ListView):
    model = Event
    template_name = "events/event_list.html"
    context_object_name = "events"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        all_events = Event.objects.all().order_by('date')

        upcoming_events = []
        past_events = []
        for event in all_events:
            if event.date > now.date() or (event.date == now.date() and event.time and event.time > now.time()):
                upcoming_events.append(event)
            else:
                past_events.append(event)

        context['upcoming_events'] = upcoming_events
        context['past_events'] = past_events
        return context

class EventDetailView(DetailView):
    model = Event
    template_name = "events/event_detail.html"
    context_object_name = "event"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        event = self.get_object()
        now = timezone.now()
        if event.date < now.date() or (event.date == now.date() and event.time and event.time <= now.time()):
            is_past_event = True
        else:
            is_past_event = False
            
        ctx["is_past_event"] = is_past_event
        ctx["registration_form"] = EventRegistrationForm()
        ctx['gallery_images'] = event.gallery.all()
        return ctx

@login_required
def register_for_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    now = timezone.now()
    if event.date < now.date() or (event.date == now.date() and event.time and event.time <= now.time()):
        return redirect("event_detail", pk=pk)

    EventRegistrationForm(request.POST or None)
    EventRegistration.objects.get_or_create(event=event, user=request.user)
    return redirect("event_detail", pk=pk)
