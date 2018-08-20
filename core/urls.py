from django.conf.urls import url
from views import LogInView

urlpatterns = [
	url(r'^login$', LogInView.as_view()),
]