from django.shortcuts import render
from datetime import datetime


def index(request):
    """Render the adcs index template with a simple context."""
    return render(request, 'adcs/index.html', {'year': datetime.now().year})


def home(request):
    """Render the home page template."""
    return render(request, 'adcs/home.html')

def gallery(request):
	"""Render the gallery page template."""
	return render(request, 'adcs/gallery.html')

def contact(request):
	"""Render the contact page template."""
	return render(request, 'adcs/contact.html')	

def about(request):
	"""Render the about page template."""
	return render(request, 'adcs/about.html')	


