from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'master$', views.master_template),
]