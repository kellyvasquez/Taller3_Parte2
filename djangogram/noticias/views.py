from django.shortcuts import render
from django.http import HttpResponse

def listar_noticias(request):
	return render(request, 'noticias/noticias.html')

# Create your views here.
