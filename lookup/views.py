from django.shortcuts import render


# Create your views here.

def home (request): #named after home html page
	return render(request, 'home.html', {}) # directed to the home.html page
def about (request): #named after home html page
	return render(request, 'about.html', {}) # directed to the home.html page
