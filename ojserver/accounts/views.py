from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse


from django.contrib.auth.hashers import make_password
from django.utils.timezone import now

from .models import Account
import json



from django.contrib.auth.models import User

# Create your views here.

def login(request):
    return HttpResponse("sdfgh")


def register(request):
    if(request.method != "POST"):
        return JsonResponse({'status':'Please Follow Documentation'})
    # user = User.objects.get(username='pushpendrahpx')
    x = json.loads(request.body.decode('utf-8'))
    # print(x["username"])
    try:
        user = User.objects.create(is_superuser=False, password=make_password(x["password"]), username=x["username"], email=x["email"], is_active = True, first_name=x["firstname"], last_name=x["lastname"])
        user.save()

        account = Account(user=user, created_at=now,code='INAUGRATION', rating=0)
        account.save()

        return JsonResponse({'email':user.email,'status':'user success'})
    except ObjectDoesNotExist:
        user=None
        return JsonResponse({'status':'usernotfound'})