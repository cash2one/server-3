import datetime

from django.utils import translation

from django.contrib.auth.hashers import PBKDF2PasswordHasher,make_password
from django.core.paginator import Paginator,PageNotAnInteger,InvalidPage,EmptyPage

def avator_path(instance,filename):
    name = datetime.datetime.now().strftime("%Y-%m-%d %H:%I:%S")

    return 'avator/%s.jpg' % name

def serials_path(instance,filename):
    return 'serials/%s' % filename

def makepassword(instance):
    hasher = PBKDF2PasswordHasher()
    key = hasher.encode(password=instance,salt="pbkdf2_sha256",iterations=5000)
    return key

def pagination(request, queryset, display_amount=10, after_range_num = 5,befor_range_num = 4):
    paginator = Paginator(queryset, display_amount)
    if  'page' not in request.GET:
        page = 1
    else:
        try:
            page = int(request.GET.get('page'))
            if page < 1:
                page = 1
            elif page > paginator.num_pages:
                page = paginator.num_pages
        except ValueError:
            page = 1

    page_count = paginator.num_pages

    try:
        objects = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        objects = paginator.page(paginator.num_pages)

    if page >= after_range_num:
        page_range = list(paginator.page_range)[page - after_range_num:page + befor_range_num]
    else:
        page_range = list(paginator.page_range)[0:int(page) + befor_range_num]
    return objects,page_range,page_count