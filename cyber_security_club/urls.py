from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("events/", include("events.urls")),
    path("team/", include("team.urls")),
    path("achievements/", include("achievements.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
    path("former-presidents/", TemplateView.as_view(template_name="former_presidents.html"), name="former_presidents"),
    path("contact/", TemplateView.as_view(template_name="contact.html"), name="contact"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)