from django.db import models

# Create your models here.
class FacebookUser(models.Model):
	uid = models.CharField(max_length=255)
	access_token = models.CharField(max_length=255)

	def __str__(self):
		return str(self.uid)
		