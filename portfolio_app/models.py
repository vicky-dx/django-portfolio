from django.db import models

class Profile(models.Model):
    """
    A singleton model to store personal information and site-wide settings.
    """
    name = models.CharField(max_length=100)
    photo_url = models.URLField(blank=True, help_text="A URL to your profile picture (e.g., from a CDN or another site).")
    about_me_p1 = models.TextField(blank=True, help_text="First paragraph of your 'About Me' section.")
    about_me_p2 = models.TextField(blank=True, help_text="Second paragraph of your 'About Me' section.")
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    resume_url = models.URLField(blank=True, help_text="A link to your resume PDF.")
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    
    class Meta:
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.name

class Highlight(models.Model):
    """
    Represents a single highlight card in the 'About Me' section.
    Linked to the Profile.
    """
    profile = models.ForeignKey(Profile, related_name='highlights', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    icon_class = models.CharField(max_length=50, help_text="e.g., 'fas fa-award'")
    icon_bg_color = models.CharField(max_length=50, default='from-blue-500 to-cyan-500', help_text="e.g., 'from-blue-500 to-cyan-500'")
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.title

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    company_url = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)
    summary = models.CharField(max_length=255, help_text="A brief one-line summary of the role.")
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, help_text="Leave blank if this is your current position.")
    description = models.TextField(help_text="Enter key achievements, separated by newlines.")
    display_order = models.PositiveIntegerField(default=0, help_text="Experiences with lower numbers will appear first.")
    
    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.title} at {self.company}"

    def get_description_points(self):
        return self.description.strip().split('\n')

class Skill(models.Model):
    name = models.CharField(max_length=50)
    icon_class = models.CharField(max_length=50, help_text="e.g., 'fab fa-python'")
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.name

class AdditionalTech(models.Model):
    """
    Model for technologies listed in the 'Additional Technologies' section.
    """
    name = models.CharField(max_length=50)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Additional Technologies"
        ordering = ['display_order']

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    display_order = models.PositiveIntegerField(default=0, help_text="Projects with lower numbers will appear first.")

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.title
