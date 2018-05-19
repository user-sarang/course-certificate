from django.contrib import admin
from .models import Course, Workshop, Course_Certificate
from .models import Workshop_Certificate, Student, Certificate_Type
from .models import Course_Certificate_Type
# Register your models here.
admin.site.register(Course)
admin.site.register(Workshop)
admin.site.register(Course_Certificate)
admin.site.register(Workshop_Certificate)
admin.site.register(Student)
admin.site.register(Certificate_Type)
admin.site.register(Course_Certificate_Type)

