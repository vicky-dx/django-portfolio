from django.shortcuts import render
from .models import Profile, Project, Experience, Skill

# Create your views here.

def portfolio_view(request):
    """
    This view fetches all the necessary data from the database,
    including the new Profile information.
    """
    # Fetch all objects from the database.
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    skills = Skill.objects.all()
    
    # Fetch the first Profile object. There should only be one.
    # Using .first() prevents an error if the profile hasn't been created yet.
    profile = Profile.objects.first()

    # The context dictionary passes all data to the template.
    context = {
        'profile': profile,
        'projects': projects,
        'experiences': experiences,
        'skills': skills,
    }
    
    # Render the request with the template and the context data.
    return render(request, 'portfolio_app/index.html', context)
