from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Roles(models.TextChoices):
        SUPER_ADMIN = "SUPER_ADMIN", "Super Admin"
        FIRM_OWNER = "FIRM_OWNER", "Firm Owner"
        CONSULTANT = "CONSULTANT", "Consultant"
        CLIENT = "CLIENT", "Client"

    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.CLIENT)

    firm = models.ForeignKey(
        "firms.Firm", on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.username


class ConsultantProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="consultant_profile"
    )
    specialization = models.CharField(max_length=255)
    experience_years = models.PositiveIntegerField()
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.user.username
