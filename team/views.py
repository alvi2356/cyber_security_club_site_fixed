from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import TeamMember
from .forms import MemberPhotoUploadForm

class TeamListView(ListView):
    model = TeamMember
    template_name = "team/team_list.html"
    context_object_name = "team_members"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_members = TeamMember.objects.all().order_by('order', 'name')

        # Define committee positions (you can adjust this list)
        committee_positions = [
            'President', 'Treasurer', 'General Secretary', 'Vice President',
            'Secretary', 'Joint Secretary', 'Organizing Secretary', 'Executive Member'
        ]

        # Separate members into committee and representatives
        committee_members = []
        representative_members = []

        for member in all_members:
            if member.position in committee_positions:
                committee_members.append(member)
            else:
                representative_members.append(member)

        context['committee_members'] = committee_members
        context['representative_members'] = representative_members
        
        # Remove the original 'team_members' if you don't need it anymore in the context
        # del context['team_members']

        return context

@login_required
def upload_photo(request):
    if request.method == "POST":
        form = MemberPhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            member = form.save(commit=False)
            member.user = request.user
            member.save()
            return redirect("team_list")
    else:
        form = MemberPhotoUploadForm()
    return render(request, "team/upload_photo.html", {"form": form})
