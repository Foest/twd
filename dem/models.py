from django.db import models
from django.contrib.auth.models import User
from localflavor.us.models import USStateField
from django.template.defaultfilters import slugify
from datetime import datetime

class DemUser(models.Model):
    user = models.OneToOneField(User)
    state = USStateField(null=True, blank=True)
    monies = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Dem Users'

class Reward(models.Model):
    monies = models.IntegerField(default=100)
    title = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.title

class Proposal(models.Model):
    title = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(DemUser)
    endorsements = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.date_created = datetime.now()
        super(Proposal, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Proposals'

class Mission(models.Model):
    title = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)
    creator = models.ForeignKey(DemUser)
    date_created = models.DateTimeField(auto_now_add=True)
    #lat_coord = models.DecimalField(max_digits=9, decimal_places=6)
    #lng_coord = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.TextField(default="No Description Available")
    #reward = models.ForeignKey(Reward)
    def __str__(self):
        return self.title

class Assignment(models.Model):
    assignee = models.ForeignKey(DemUser)
    mission = models.ForeignKey(Mission)
    reward = models.ForeignKey(Reward)
    lat_coord = models.DecimalField(max_digits=9, decimal_places=6)
    lng_coord = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.mission.title
