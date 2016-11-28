#coding: utf-8

from django.shortcuts import render,render_to_response

from django.views.generic import View,TemplateView,DetailView


from django.contrib.auth.decorators import login_required,permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate,login
import json
from django.http import JsonResponse,Http404

from django.views.decorators.http import require_http_methods,require_POST
from django.views.decorators.csrf import csrf_protect,ensure_csrf_cookie,csrf_exempt
from forms import LoginForm,ManagerForm

from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db import transaction

from django.conf import settings
from TV_Server.Utils import pagination
from django.core import serializers

from Managers.models import Manager


# Create your views here.


class BackendLogin(View):
    template_name = 'login.html'

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)

    def post(self,request,*args,**kwargs):
        form = LoginForm(data=request.POST)

        if form.is_valid():

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email,password=password)
            if user is not None:
                login(request,user)
                result = {"status": "success", "result": "/backend/index/"}
                return JsonResponse(result)
        result = {"status":"error","result": "用户名或密码错误"}
        return JsonResponse(result)


class BackendHome(LoginRequiredMixin,TemplateView):
    template_name = "manager.html"

    def get(self,request,*args,**kwargs):
        managers = Manager.custom.add_images_url()


        user = request.user
        if not user.headshot.name.strip():
            avator_path = ''
        else:
            avator_path = settings.ALLOWED_HOSTS[0] + user.headshot.url

        objects, page_range,page_count = pagination(request, managers)
        head_list = ["id","headshot","email","nickname"]

        return render(request, self.template_name, {'objects': objects,'user':user,'headshot':avator_path,'page_count':page_count ,'page_range': page_range,"table_title":"Manager List","head_list":head_list})

@login_required()
def manager_detail(request,itemid):
    try:
        itemid = int(itemid)
        manager = Manager.custom.get_single(pk=itemid)
        if manager:
            data=serializers.serialize("json", manager)
            return render(request,"manager_detail.html",{"object":data})
    except ValueError:
        return Http404()












### Manager ###

@login_required()
@require_POST
def save_manager(request):
    if request.method == "POST":

        form = ManagerForm(request.POST,request.FILES)
        print form.errors
        if form.is_valid():

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            nickname = form.cleaned_data['nickname']
            headshot = request.FILES['headshot']
            is_superuser = form.cleaned_data['is_superuser']
            manager = Manager(email=email,password=password,nickname=nickname,headshot=headshot,is_superuser=is_superuser)
            manager.save()

            return JsonResponse({"status":"success"})
    return JsonResponse({"status":"error"})



@login_required()
@require_http_methods(["GET"])
def delete_data_manager(request):
    if request.method == "GET":
        ids = request.GET.getlist('item')
        for item in ids:
            manager = Manager.objects.get(pk=item)
            if manager:
                with transaction.atomic():
                    manager.delete()
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error"})

@login_required()
@require_POST
@csrf_protect
def alterManager(request):
    if request.method == "POST":
        userid = request.POST['userid']
        superuser = request.POST['is_superuser']

        if userid:
            manager = Manager.objects.get(pk=userid)

            if manager:
                if superuser == "true":
                    manager.is_superuser = True
                else:
                    manager.is_superuser = False
                manager.save()

                return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error"})


