from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100, help_text="FontAwesome icon class")
    process_steps = models.JSONField(default=list, help_text="List of process steps")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class DemoProject(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='demo_projects')
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='demo_projects/')
    tags = models.JSONField(default=list, help_text="List of tags")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
