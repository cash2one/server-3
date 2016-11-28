from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView

from Managers.forms import ManagerForm
from Serials.forms import SerialsForm
from Serials.models import Serials
from TV_Server.Utils import pagination
from Tags.models import Tag

class SerialList(LoginRequiredMixin,TemplateView):
    template_name = "serials.html"

    def get(self, request, *args, **kwargs):
        tags = Tag.objects.all()
        serials = Serials.custom.add_images_url()
        objects, page_range, page_count = pagination(request, serials)
        head_list = ["id", "headshot", "title"]
        if tags:
            return render(request, self.template_name, {"tags": tags,'objects': objects,'page_count':page_count ,'page_range': page_range,"table_title":"Manager List","head_list":head_list})



@login_required()
@require_POST
def save_serials(request):
    form = SerialsForm(request.POST, request.FILES)
    if form.is_valid():
        title = form.cleaned_data['title']
        describe = form.cleaned_data['describe']
        director = form.cleaned_data['director']
        actors = form.cleaned_data['actors']

        tag = form.cleaned_data['catagory']


        type = form.cleaned_data['type']

        headshot = request.FILES['headshot']

        serial = Serials.objects.create(title=title,describe=describe,director=director,actors=actors,type=type,headshot=headshot)
        serial.catagory.add(tag[0])



        serial.save()

        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error"})