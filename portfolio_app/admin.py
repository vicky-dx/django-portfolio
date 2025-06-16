from django.contrib import admin
from .models import Profile, Highlight, Project, Tag, Experience, Skill, AdditionalTech

class HighlightInline(admin.TabularInline):
    """
    Allows editing of Highlights directly within the Profile admin page.
    """
    model = Highlight
    extra = 1 # Shows one extra blank form for a new highlight
    ordering = ('display_order',)

class ProfileAdmin(admin.ModelAdmin):
    """
    Customizes the admin interface for the Profile model.
    """
    inlines = [HighlightInline]

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
admin.site.register(AdditionalTech, AdditionalTechAdmin)
admin.site.register(Tag, TagAdmin)
# We don't register Highlight directly as it's an inline
