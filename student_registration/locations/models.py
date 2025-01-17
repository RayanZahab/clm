from __future__ import unicode_literals, absolute_import, division

from django.db import models
from model_utils import Choices
from model_utils.models import TimeStampedModel
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext as _
from django.contrib.gis.db import models


class LocationType(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Location Type'

    def __unicode__(self):
        return self.name


class Location(MPTTModel):

    name = models.CharField(max_length=254)
    type = models.ForeignKey(LocationType, verbose_name='Location Type')
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    p_code = models.CharField(max_length=32, blank=True, null=True)

    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    def __unicode__(self):
        return u'{}'.format(
            self.name
        )

    class Meta:
        unique_together = ('name', 'type', 'p_code')
        ordering = ['name']
