from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^course-certificate$', views.course_certificate, name='course_certificate'),
    url(r'^workshop-certificate$', views.workshop_certficate, name='workshop_certificate'),
]