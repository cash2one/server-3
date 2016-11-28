from django.conf.urls import url

from views import BackendLogin,BackendHome

from views import save_manager,delete_data_manager,manager_detail,alterManager


urlpatterns = [
    url(r'^login/$',BackendLogin.as_view(),name="login"),
    url(r'^index/$',BackendHome.as_view(),name="index"),



    url(r'^addmanager/$', save_manager,name="addmanager"),
    url(r'^delete_data/$', delete_data_manager),
    url(r'^manager/detail/(\d+)/$',manager_detail),
    url(r'^alterManager/$',alterManager),
]