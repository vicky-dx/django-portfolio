from django.contrib import admin
from .models import Profile, Project, Tag, Experience, Skill, AdditionalTech

# We will create custom admin classes to improve the interface.

class ProfileAdmin(admin.ModelAdmin):
    pass

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_order')
    list_filter = ('tags',)
    search_fields = ('title', 'description')
    filter_horizontal = ('tags',)
    ordering = ('display_order',)

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date')
    search_fields = ('title', 'company', 'description')
    ordering = ('-start_date',)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_order')
    search_fields = ('name', 'icon_class')
    ordering = ('display_order',)

class AdditionalTechAdmin(admin.ModelAdmin):
    """
    Customizes the admin interface for the AdditionalTech model.
    """
    list_display = ('name', 'display_order')
    search_fields = ('name',)
    ordering = ('display_order',)

class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)

# Register your models with the admin site.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(AdditionalTech, AdditionalTechAdmin) # Register the new model
admin.site.register(Tag, TagAdmin)
