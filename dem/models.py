from django.db import models
from django.contrib.auth.models import User
from localflavor.us.models import USStateField

class DemUser(models.Model):
    user = models.OneToOneField(User)
    state = USStateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Dem Users'
