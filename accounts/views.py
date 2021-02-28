from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import *

def index(request):
	return HttpResponse("Hello, you have found the accounts index.")

def create(request):
	inputName = request.GET.get('name')
	inputEmail = request.GET.get('email')
	inputWallet = request.GET.get('wallet')
	inputProfits = request.GET.get('profits')
	inputCountry = request.GET.get('country')
	inputBalance = request.GET.get('balance')
	inputInterest = request.GET.get('interest')
	# Check to make wallet is not already in the database
	try:
		wallet = Account.objects.get(wallet_address=inputWallet)
	except:
		# Wallet not found in database, instantiating new account
		NewAccount = Account(name=inputName, email=inputEmail, wallet_address=inputWallet, profits=inputProfits, country_code=inputCountry, current_balance=inputBalance, interest_rate=inputInterest)
		NewAccount.save()
		return HttpResponse("Account reigstered with wallet address: " + inputWallet)
	# This gets sent when an existing account is found
	return HttpResponse("Wallet already associated with an account")

def read(request):
	input_wallet = request.GET.get('wallet')
	try:
		account = Account.objects.get(wallet_address=input_wallet)
		print(account)
		return HttpResponse(account)
	except:
		return HttpResponse("Account not found")
