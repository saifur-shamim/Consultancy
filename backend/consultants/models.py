from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class ConsultantAvailability(models.Model):
    consultant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="availability_slots",
        limit_choices_to={"role": "CONSULTANT"},
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_booked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["start_time"]
        unique_together = ("consultant", "start_time", "end_time")

    def __str__(self):
        return f"{self.consultant} | {self.start_time} - {self.end_time}"
