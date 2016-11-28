from django.conf.urls import url

from Videos.views import VidelList,VideoAdd,test

urlpatterns = [

    url(r'^videos/$', VidelList.as_view(), name="videos"),
    url(r'^test/$',test),
    url(r'^videos/addvideo/$', VideoAdd.as_view()),
]


# http://baobab.wandoujia.com/api/v3/videos?_s=b5d80ddf05d91632386b9f57dd437307&categoryId=12&f=iphone&net=wifi&num=20&start=0&strategy=date&u=1ae6c0b4c0a8a32dd5aaaba2ee4aacda9f84bc5d&v=2.0.0&vc=522