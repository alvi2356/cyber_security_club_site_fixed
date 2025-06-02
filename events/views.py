from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView
from .models import Event
from .forms import EventRegistrationForm
from .models import Event, EventRegistration
from django.utils import timezone
from django.contrib import messages
from django.http import JsonResponse, HttpResponse

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

@login_required
def register_for_event(request, pk):
    if request.method == 'POST':
        event = get_object_or_404(Event, pk=pk)
        now = timezone.now()

        if event.date < now.date() or (event.date == now.date() and event.time and event.time <= now.time()):
            return JsonResponse({'status': 'error', 'message': 'This event has already occurred.'}, status=400)

        existing_registration = EventRegistration.objects.filter(event=event, user=request.user).exists()

        if existing_registration:
            return JsonResponse({'status': 'info', 'message': 'You are already registered for this event.'})
        else:
            EventRegistration.objects.create(event=event, user=request.user)
            return JsonResponse({'status': 'success', 'message': 'Thanks for registering! Further details will be mailed very soon.'})

    return HttpResponse("Method not allowed", status=405)
