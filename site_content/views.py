from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from site_content.models import Experience, Skill, Project


# Create your views here.
def get_experiences(request):
    experience = Experience.objects.values()
    return JsonResponse(dict([("experiences", list(experience))]))

def get_skills(request):
    skill = Skill.objects.values()
    return JsonResponse(dict([("skills", list(skill))]))

def get_projects(request):
    project = Project.objects.values()
    return JsonResponse(dict([("projects", list(project))]))