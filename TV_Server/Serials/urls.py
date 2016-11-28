
from django.conf.urls import url

from views import SerialList,save_serials

urlpatterns = [
    url(r'^serials/$', SerialList.as_view(), name="serials"),
    url(r'^addserials/$',save_serials),
]

