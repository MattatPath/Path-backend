from django.db import models

class Account(models.Model):
	name = models.CharField(max_length=42, default="None")
	email = models.CharField(max_length=42, default="NEED TO FORMAT EMAIL")
	wallet_address = models.CharField(max_length=42, primary_key=True)
	profits = models.CharField(max_length=42, default="0.00")
	country_code = models.CharField(max_length=2, default="NO")
	current_balance = models.CharField(max_length=10, default="0.00")
	interest_rate = models.CharField(max_length=10, default="0.01")

	def __str__(self):
		return '{}-{}-{}-{}-{}-{}-{}'.format(self.name, self.email, self.wallet_address, self.profits, self.country_code, self.current_balance, self.interest_rate)
