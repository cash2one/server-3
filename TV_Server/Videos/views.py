from django.http import JsonResponse,HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.conf import settings

from Videos.forms import VideoAddForm

from Serials.models import Serials
from Videos.models import Video

from TV_Server.Utils import pagination


class VidelList(TemplateView):
    template_name = "videos.html"

    def get(self, request, *args, **kwargs):
        host = settings.ALLOWED_HOSTS[0]+"/backend/addvideo/"
        videos = Video.videos.all()
        objects, page_range, page_count = pagination(request, videos)
        return render(request, self.template_name, {"host":host,'objects': objects,'page_count':page_count ,'page_range': page_range,"head_list": ["title", "manager_id","serials","video_url"]})


class VideoDetail(TemplateView):
    template_name = "video_detail.html"

class VideoAdd(TemplateView):
    template_name = "add_video.html"

    def get(self, request, *args, **kwargs):
        serials = Serials.objects.all()
        return render(request,self.template_name,{"serials":serials})

    def post(self, request, *args, **kwargs):

        form = VideoAddForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            describe = form.cleaned_data['describe']
            video_url = request.FILES['video_url']
            serials = form.cleaned_data['serials']

            print 'file===%s   %s' % (video_url.name,video_url.temporary_file_path)

            manager = request.user

            video = Video.objects.create(title=title,describe=describe,video_url=video_url,manager=manager,serials=serials)



            return JsonResponse({"status": "success"})
        return JsonResponse({"status": "error"})


def test(request):
    path = settings.ALLOWED_HOSTS[0]+settings.MEDIA_URL+'test/'+'test.m3u8'
    print path
    return JsonResponse({'url':path})