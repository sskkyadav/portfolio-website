from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    message = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    rating = models.IntegerField(default=5, choices=[(i, i) for i in range(1, 6)])
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.designation}"
