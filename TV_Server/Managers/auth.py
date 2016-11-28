#coding: utf-8

from django.conf import settings
from django.contrib.auth.hashers import check_password


from models import Manager

class Authentication(object):

    def authenticate(self,email,password):
        if not(any(email) and any(password)):
            return None

        try:
            manager = Manager.objects.get(email=email)
            if manager is not None:
                key = manager.password
                pwd_valid = check_password(password,key)
                if pwd_valid:
                    return manager
            return None
        except Manager.DoesNotExist:
            return None


    def get_user(self,user_id):
        try:
            return Manager.objects.get(pk=user_id)
        except Manager.DoesNotExist:
            return None