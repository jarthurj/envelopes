from django.db import models
from django.contrib.auth.models import User
class Envelope(models.Model):
	name = models.CharField(max_length=100)
	user = models.ForeignKey(User, related_name='users')
	total = models.DecimalField(decimal_places=2)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Transaction(models.Model):
	name = models.CharField(max_length=100)
	total = models.DecimalField(decimal_places=2)
	envelope = models.ForeignKey(Envelope, related_name='envelopes')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
