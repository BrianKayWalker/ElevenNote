# Python imports
from datetime import timedelta

# Django imports
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from tastypie.models import create_api_key

# Create your models here.
class Note(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - timedelta(days=1) <= self.pub_date <= now


# Make a tastypie API key whenever a new user is created.
models.signals.post_save.connect(create_api_key, sender=User)
