from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'html/home.html')

def about(r):
	return render(r,'html/about.html')

def contact(r):
	return render(r,'html/contactus.html')

def login(r):
	return render(r,'html/login.html')