"""Define the urls for the site contents."""

from django.urls import path
from site_content.views import get_experiences, get_skills, get_projects

urlpatterns = [
    path('get-experiences/', get_experiences, name="get_experiences"),
    path('get-skills/', get_skills, name="get_skills"),
    path('get-projects/', get_projects, name="get_projects"),
]