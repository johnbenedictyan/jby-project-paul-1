from django.conf.urls import url
from .views import admin_panel,follow_up,sign_up,sign_in,sign_out

urlpatterns = [
    url(r'^$', admin_panel, name="admin_panel_link"),
    url(r'^follow_up/(?P<fault_id>\d+)$', follow_up, name="follow_up_link"),
    url(r'^sign_up/$', sign_up, name="sign_up_link"),
    url(r'^sign_in/$', sign_in, name="sign_in_link"),
    url(r'^sign_out/$', sign_out, name="sign_out_link")
]
