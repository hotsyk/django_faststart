# -*- coding: utf-8 -*-
from django.db import models

class Model1 (models.Model):
    """
    This is model for the object1
    """

    pass

    class Meta:
        pass

    def __unicode__(self):
        return ""

    def get_absolute_url(self):
        return ""
