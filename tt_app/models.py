from django.db import models
from django.contrib.auth.models import User

class Timesheet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="timesheets")
    description = models.TextField(blank=True)
    rate = models.FloatField()
    total_time = models.IntegerField(null=True, blank=True)
    total_cost = models.FloatField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.pk:
            self.total_time = sum (entry.minutes for entry in self.entries_set.all())
            self.total_cost = self.rate * self.total_time
        super().save(*args, **kwargs)


class LineItem(models.Model):
    timesheet = models.ForeignKey(Timesheet, on_delete=models.CASCADE, related_name="entries")
    date = models.DateTimeField()
    minutes = models.IntegerField()