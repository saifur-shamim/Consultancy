from django.db import models
from django.conf import settings


class Appointment(models.Model):
    consultant = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="consultations"
    )
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="appointments"
    )
    firm = models.ForeignKey("firms.Firm", on_delete=models.CASCADE)

    availability = models.OneToOneField(
        "consultants.ConsultantAvailability",
        on_delete=models.PROTECT,
        related_name="appointment",
    )

    scheduled_at = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=[
            ("PENDING", "Pending"),
            ("CONFIRMED", "Confirmed"),
            ("COMPLETED", "Completed"),
            ("CANCELLED", "Cancelled"),
        ],
        default="PENDING",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client} → {self.consultant} ({self.scheduled_at})"
