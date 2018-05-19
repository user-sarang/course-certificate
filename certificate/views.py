from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'certificate/home.html', {})


def course_certificate(request):
	return render(request, 'certificate/course_certificate.html', {})	


def workshop_certficate(request):
	return render(request, 'certificate/workshop_certificate.html', {})