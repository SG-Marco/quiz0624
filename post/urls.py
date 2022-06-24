from django.contrib import admin
from django.urls import path, include
from .views import SkillView, JobView, JobPostView

urlpatterns = [
    path('', SkillView.as_view()),
    path('job', JobView.as_view()),
    path('jobpost', JobPostView.as_view()),
]
