from django.shortcuts import render
from .models import FormerPresident

def former_presidents_view(request):
    former_presidents = FormerPresident.objects.all()
    return render(request, 'former_presidents.html', {
        'former_presidents': former_presidents
    })
