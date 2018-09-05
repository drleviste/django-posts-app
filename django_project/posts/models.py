# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from datetime import datetime

from django.db import models

# Create your models here.


class Posts(models.Model):
    title = models.CharField(unicode(_("")), max_length=200)
    body = models.TextField(unicode(_("")))
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Posts'
