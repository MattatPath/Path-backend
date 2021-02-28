from django.db import models

class Transaction(models.Model):
	amount = models.CharField(max_length=20, default="0.00")
	date = models.CharField(max_length=8, default="DATE")
	identification = models.CharField(max_length=20, default="ID LENGTH?")
	status = models.CharField(max_length=20, default="status pending")
