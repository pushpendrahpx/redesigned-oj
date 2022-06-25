from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

import json
import subprocess 





def addNewProblem(request):
    return HttpResponse("sdfgh")

def executeCode(request):
    x = request.body.decode('utf-8')
    f = open('code.cpp','w')
    f.write(x)
    f.close()
    comp = subprocess.run(["g++.exe",  "code.cpp"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # output = None
    if(comp.returncode != 0):
        return HttpResponse(comp.stderr, status=400)



    output = subprocess.run(["a.exe"], stdout=subprocess.PIPE)
    # f.close()
    return HttpResponse(output.stdout)

