from django.urls import path

from myPage.views import *

app_name = "resume"

urlpatterns = [
    path("", resume_view, name="resume-view"),
]
