from django.conf.urls import url
from .views import admin_panel,follow_up

urlpatterns = [
    url(r'^$', admin_panel, name="admin_panel_link"),
    url(r'^follow_up/(?P<fault_id>\d+)$', follow_up, name="follow_up_link"),
]
