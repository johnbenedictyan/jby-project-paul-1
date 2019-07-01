from django.conf.urls import url
from .views import fault_submission

urlpatterns = [
    url(r'^$', fault_submission, name="fault_submission_link"),
]
