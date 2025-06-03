from django.shortcuts import render, redirect
# from django.conf import settings # Removed as we'll get status from model
from .forms import RecruitmentApplicationForm
from .models import RecruitmentSetting # Import the new model

# Create your views here.

def recruit_view(request):
    # Get the single recruitment setting instance, default to active if none exists
    try:
        recruitment_setting = RecruitmentSetting.objects.get()
        recruitment_active = recruitment_setting.is_active
    except RecruitmentSetting.DoesNotExist:
        # If no setting exists, assume recruitment is inactive or handle as desired
        # For now, let's default to inactive if no setting is explicitly created
        recruitment_active = False

    if not recruitment_active:
        return render(request, 'recruitment/recruitment_closed.html', {'message': 'Recruitment is not currently active. Please check back later.'})

    if request.method == 'POST':
        form = RecruitmentApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or show a success message
            return render(request, 'recruitment/recruit_success.html')
    else:
        form = RecruitmentApplicationForm()

    context = {
        'form': form,
    }
    return render(request, 'recruitment/recruit.html', context)
