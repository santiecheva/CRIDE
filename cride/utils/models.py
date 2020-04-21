""" Django models utilitys """

# Django

from django.db import models

class CRideModel(models.Model):
""" Compart Ride Base Model.

	CRideModel acts as an abstract base class from wghich every 
	other model in the project will inherit. this Class provides every table with the
	following with the following attributes:
		+ created (DateTime): store the datetime the object was created.
		+ modified (DateTime): Store the last datetime the object was modified. 
"""

	created = models.DateTimeField(
		'created at'
		auto_now_add= True,
		help_text = 'Date time on which the object was created'
	 	)

	modified = models.DateTimeField(
		'modified at'
		auto_now = True,
		help_text = 'Date time on which the object was last modified'
	 	)

	class Meta:
		abstract = True
		get_lastet_by = 'created'
		ordering = ['-created','-modified']