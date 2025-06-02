from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as account_views  # Import your views module

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("events/", include("events.urls")),
    path("team/", include("team.urls")),
    path("achievements/", include("achievements.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
    path("former-presidents/", include("former_presidents.urls")),
    path("contact/", account_views.contact_view, name="contact"),
    path('recruitment/', include('recruitment.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)