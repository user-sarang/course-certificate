from django.shortcuts import render
from .models import Course, Workshop, Course_Certificate
from .models import Workshop_Certificate, Student, Certificate_Type
from .models import Course_Certificate_Type
from .forms import UserList
import logging
# Create your views here.
def home(request):
	return render(request, 'certificate/home.html', {})

def course_certificate(request):
	container ={}
	
	container['courses'] = Course.objects.all()
	container['certificates'] = Course_Certificate.objects.all()

	if request.method == "POST":
		form = UserList(request.POST, request.FILES)
		csv_file = request.FILES['user_list']

		if form.is_valid():
			process_csv(csv_file)

	return render(request, 'certificate/course_certificate.html', {'data': container})	

def workshop_certficate(request):
	return render(request, 'certificate/workshop_certificate.html', {})


def line_is_valid(line):
	if len(line) > 0: return True
	return False

def process_csv(csv_file):
	if not csv_file.name.endswith('.csv'):
		messages.error(request,'File is not CSV type')
	
	file_data = csv_file.read().decode("utf-8")
	lines = file_data.split("\n")

	for line in lines:
		if line_is_valid(line):
			fields = line.split(",")
						
			student_name = fields[0]
			student_email = fields[1]

			student = Student(student_name = student_name, student_email = student_email)

			student.save()
	

	


