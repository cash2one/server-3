from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from django.shortcuts import render,render_to_response
from django.views.decorators.http import require_POST

from django.views.generic import View
from django.views.generic import TemplateView

from TV_Server.Utils import pagination

from Tags.models import Tag
from Managers.models import Manager


class TagList(TemplateView):
    template_name = "tags.html"

    def get(self, request, *args, **kwargs):
        tags = Tag.tags.all()

        objects,page_range,page_count = pagination(request,tags)

        return render(request, self.template_name,
                      context={'objects': objects,'page_count':page_count ,'page_range': page_range,"table_title": "Manager List", "head_list": ["title", "manager_id","created_at"] })


@login_required()
@require_POST
def addtag(request):
    if request.method == "POST":
        title = request.POST['title']
        manager = request.user
        if manager and title:
            Tag.objects.create(title=title,manager=manager)
            return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error"})