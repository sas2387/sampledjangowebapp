from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(model.Model):
	"""
		Product model
	"""
	name = models.CharField(max_length=30, blank=False)
	description = models.CharField(max_length=150, blank=False)

	def __str__(self):
		return self.name