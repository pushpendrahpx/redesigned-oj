import json
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User as UserModel
from django.contrib.auth import authenticate, login as LibraryLogin, logout as LibraryLogout
from django.forms.models import model_to_dict

from .models import User 


def register(request):
    try:
        if(request.method != "POST"):
            return JsonResponse({'status':'Invalid Register Method'}, status=400)
        
        jsonData = json.loads(request.body)

        if("username" in jsonData and "email" in jsonData and "password" in jsonData and "firstname" in jsonData and "lastname" in jsonData):
            newuser = UserModel.objects.create_user(jsonData["username"], jsonData["email"],jsonData["password"],first_name=jsonData["firstname"], last_name=jsonData["lastname"], is_active=False)
            ourUserModel = User.objects.create(user=newuser, rating=0, status=True, country='India')
            print(newuser)

            return JsonResponse({'message':'user created'}, status=200)
        
        return JsonResponse({'status':'user Registration didn\'t worked doesnt created in both tables'}, status=400)
        
    except Exception as e: 

        return JsonResponse({'status':'Register EXCEPTION OCCURED', 'exception':str(e)}, status=400)

def login(request):
    try:
        if(request.method != "POST"):
            return JsonResponse({'status':'Invalid Register Method'}, status=400)
        
        jsonData = json.loads(request.body)

        if(("username" in jsonData and "password" in jsonData) != True):
            return JsonResponse({'message':'required fields username,password missing'}, status=400)

        username = jsonData["username"]
        password = jsonData["password"]
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            loginuserobj = LibraryLogin(request, user)
            print(loginuserobj)

            return JsonResponse({'message':'Login Successfull', 'object': model_to_dict(user)})
        else:
            # Return an 'invalid login' error message.
            ...
            return JsonResponse({'message':'Login Failed'})

    except Exception as e: 

        return JsonResponse({'status':'Login EXCEPTION OCCURED', 'exception':str(e)}, status=400)


def logout(request):
    try:
        if(request.method != "POST"):
            return JsonResponse({'status':'Invalid Register Method'}, status=400)
        
        if request.user.is_authenticated:
            LibraryLogout(request)
            # Do something for authenticated users.
            return JsonResponse({'message':'logout sucessfull'}, status=200)


        else:
            # Do something for anonymous users
            return JsonResponse({'message':'authentication failed'}, status=400)

    except Exception as e: 
        return JsonResponse({'status':'Logout EXCEPTION OCCURED', 'exception':str(e)}, status=400)


def getProfile(request):
    try:
        if(request.method != "GET"):
            return JsonResponse({'status':'Invalid Register Method'}, status=400)
        
        if request.user.is_authenticated:
            print("token authenticated")
            # Do something for authenticated users.
            return JsonResponse((model_to_dict(request.user)), safe=False)


        else:
            print("token authentication failed")
            # Do something for anonymous users
            return JsonResponse({'message':'authentication failed'})

    except Exception as e: 
        return JsonResponse({'status':'getProfile EXCEPTION OCCURED', 'exception':str(e)}, status=400)

