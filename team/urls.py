from django.urls import path
from .views import TeamListView, upload_photo

urlpatterns = [
    path("", TeamListView.as_view(), name="team_list"),
    path("upload/", upload_photo, name="team_upload"),
]
