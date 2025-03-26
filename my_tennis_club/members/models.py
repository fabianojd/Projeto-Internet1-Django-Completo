from django.db import models

class Member(models.Model):
    plan = models.ForeignKey("plans.Plan", on_delete=models.CASCADE, default=1)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, null=True, blank=True)
    joined_date = models.DateField(null=True, blank=True)
    foto = models.ImageField(upload_to='images/', null=True, blank=True)
    documento = models.FileField(null=True, blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
