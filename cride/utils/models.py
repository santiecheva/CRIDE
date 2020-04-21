""" Django models utilitys """

# Django

from django.db import models

class CRideModel(models.Model):

    created = models.DateTimeField(
        'created at',
        auto_now_add= True,
        help_text = 'Date time on which the object was creadooo'
        )

    modified = models.DateTimeField(
        'modified at',
        auto_now = True,
        help_text = 'Date time on which the object was last modified'
        )

    class Meta:
        
        abstract = True
        #get_lastet_by = 'created'
        ordering = ['-created','-modified']