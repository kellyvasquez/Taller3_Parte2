from django.shortcuts import render

def login(request):
	return render(request, 'users/login.html')

def registro(request):
	return render(request, 'users/registro.html')

# Create your views here.
