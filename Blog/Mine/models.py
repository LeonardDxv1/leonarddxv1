from django.db import models
from django.utils import timezone


class VisitorCount(models.Model):
    ip_address = models.GenericIPAddressField()
    visit_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Visit from {self.ip_address} at {self.visit_time}'
