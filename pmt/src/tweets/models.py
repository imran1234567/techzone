from __future__ import unicode_literals

from django.conf import settings
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.db import models
from .validators import validate_content

# Create your models here.

# def validate_content(value):
#     content = value
#     if content == "abc":
#         raise ValidationError("Content cannot be abc")
#     return value


class Tweet(models.Model):
    user        =   models.ForeignKey(settings.AUTH_USER_MODEL)
    img         = models.FileField(null=True, blank=True)
    content     =   models.CharField(max_length=140, validators=[validate_content])
    code        =   models.CharField(max_length=400)
    update      =   models.DateTimeField(auto_now=True)
    timestamp   =   models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)



    def get_absolute_url(self):
        return reverse("tweet:detail", kwargs = {"pk":self.pk})

    # def clean(self, *args, **kwargs):
    #     content = self.content
    #     if content == "abc":
    #         raise ValidationError("Cannot be abc")
    #     return super(Tweet, self).clean(*args, **kwargs)

