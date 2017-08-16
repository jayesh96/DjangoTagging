from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Annotations(models.Model):
	src =  models.CharField(max_length=300)
	text = models.CharField(max_length=300)
	shape_type =  models.CharField(max_length=300)
	x = models.DecimalField(decimal_places=10, max_digits=20)
	y = models.DecimalField(decimal_places=10, max_digits=20)
	width = models.DecimalField(decimal_places=10, max_digits=20)
	height = models.DecimalField(decimal_places=10, max_digits=20)


	def __unicode__(self):
		return str(self.text)

	def __str__(self):
		return str(self.text)

	class Meta:
		verbose_name = "Annotation"
		verbose_name_plural = "Annotations"