from django.views.generic import ListView
from .models import Achievement

class AchievementListView(ListView):
    model = Achievement
    template_name = "achievements/achievement_list.html"
    context_object_name = "achievements"
