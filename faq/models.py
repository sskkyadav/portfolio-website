from django.db import models

class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()
    category = models.CharField(max_length=50, choices=[
        ('services', 'Services'),
        ('training', 'Training'),
        ('technical', 'Technical'),
        ('pricing', 'Pricing'),
    ], default='services')
    additional_info = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'created_at']

    def __str__(self):
        return self.question
