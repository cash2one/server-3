from django.conf.urls import url

from views import TagList,addtag

urlpatterns = [
    url(r'^tags/$', TagList.as_view(), name="tags"),
    url(r'^addtag/$',addtag),
]