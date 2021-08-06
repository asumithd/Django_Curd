from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	return render(request, "home.html",{})

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html",{})

def about_view(request, *args, **kwargs):
	my_context={
	"title":"sumith This is about us",
	"my_html":"Hi Sumith",
	"my_number": 123,
	"my_list":[143,753,888,"Sumith"]

	}
	return render(request, "about.html",my_context)

def social_view(request, *args, **kwargs):
	return render(request, "social.html",{})