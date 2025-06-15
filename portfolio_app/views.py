from django.shortcuts import render
from .models import AdditionalTech, Profile, Project, Experience, Skill

import os
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.

def portfolio_view(request):
    """
    This view fetches all the necessary data from the database,
    including the new Profile and AdditionalTech information.
    """
    # Fetch all objects from the database.
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    skills = Skill.objects.all()
    additional_technologies = AdditionalTech.objects.all()
    
    # Fetch the first Profile object.
    profile = Profile.objects.first()

    # The context dictionary passes all data to the template.
    context = {
        'profile': profile,
        'projects': projects,
        'experiences': experiences,
        'skills': skills,
        'additional_technologies': additional_technologies,
    }
    
    # Render the request with the template and the context data.
    return render(request, 'portfolio_app/index.html', context)


def create_admin_user(request):
    username = os.getenv("ADMIN_USERNAME")
    password = os.getenv("ADMIN_PASSWORD")
    email = os.getenv("ADMIN_EMAIL")

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        return HttpResponse("✅ Admin user created.")
    return HttpResponse("⚠️ Admin user already exists.")