""" Django models utilitys """

# Django

from django.db import models

class CRideModel(models.Model):

    created = models.DateTimeField(
        'created at',
        auto_naw_add= True,
        help_text = 'Date time on which the object was created',
        )

    modified = models.DateTimeField(
        'modified at',
        auto_naw = True,
        help_text = 'Date time on which the object was last modified'
        )

    class Meta:
        
        abstract = True
        get_lastet_by = 'created'
        ordering = ['-created','-modified']