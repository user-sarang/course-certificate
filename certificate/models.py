from django.db import models

# Create your models here.
class Course(models.Model):
	course_name = models.CharField(max_length=200)
	instructor_name = models.CharField(max_length=250)
	director_name = models.CharField(max_length=250)

class Workshop(models.Model):
	workshop_name = models.CharField(max_length=200)
	workshop_instructor_name = models.CharField(max_length=250)

class Certificate_Type(models.Model):
	certificate_type = models.CharField(max_length=255)

class Course_Certificate(models.Model):
	course_certificate_type = models.ForeignKey('certificate.Certificate_Type')
	course_name = models.ForeignKey('certificate.Course')
	course_template = models.FileField(upload_to='course_certificate_templates')

class Workshop_Certificate(models.Model):
	workshop_name = models.ForeignKey('certificate.Workshop')
	workshop_template = models.FileField(upload_to='workshop_certificate_templates')

class Student(models.Model):
	student_name = models.CharField(max_length= 255)
	student_email = models.CharField(max_length=255)