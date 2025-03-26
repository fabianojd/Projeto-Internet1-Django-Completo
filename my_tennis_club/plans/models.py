from django.db import models

class Plan(models.Model):
    title = models.CharField(max_length=60, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
