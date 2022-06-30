from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

def create_submission(request):

    # Only POST Method is accepted
    if(request.method!="POST"):
        return JsonResponse({'status':'Invalid Method'})


    print(request.body)


    return HttpResponse('Hello index submissions')
