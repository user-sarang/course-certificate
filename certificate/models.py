from django.db import models

# Create your models here.
class Course(models.Model):
	course_name = models.CharField(max_length=200)
	instructor_name = models.CharField(max_length=250)
	director_name = models.CharField(max_length=250)

	def __str__(self): return self.course_name

class Workshop(models.Model):
	workshop_name = models.CharField(max_length=200)
	workshop_instructor_name = models.CharField(max_length=250)

	def __str__(self): return self.workshop_name

class Certificate_Type(models.Model):
	certificate_type = models.CharField(max_length=255)

	def __str__(self): return self.certificate_type


class Course_Certificate_Type(Certificate_Type):
	certificate_for = models.CharField(max_length=255)

	def __str__(self): return self.certificate_for + ' (' + self.certificate_type + ')'

class Course_Certificate(models.Model):
	course_certificate_type = models.ForeignKey('certificate.Course_Certificate_Type')
	course_template = models.FileField(upload_to='course_certificate_templates')

	def __str__(self):
		return self.course_certificate_type.__str__()

class Workshop_Certificate(models.Model):
	workshop_certificate_type = models.ForeignKey('certificate.Certificate_Type')
	workshop_name = models.ForeignKey('certificate.Workshop')
	workshop_template = models.FileField(upload_to='workshop_certificate_templates')

class Student(models.Model):
	student_name = models.CharField(max_length= 255)
	student_email = models.CharField(max_length=255)