import json
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from .models import Problem


def create_problem(request):
    try:
        if(request.method != "POST"):
            return JsonResponse({'status':'Invalid create_problem Method'}, status=400)
        

        jsonData = json.loads(request.body)

        if(not("title" in jsonData and "description" in jsonData and "difficulty" in jsonData and "score" in jsonData and "tags" in jsonData and "problemcode" in jsonData and "correctoutput" in jsonData)):
            return JsonResponse({'status':'Required Fields are missing in Create Problem API'}, status=400)

        title = jsonData["title"]
        description = jsonData["description"]
        difficulty = jsonData["difficulty"]
        score = jsonData["score"]
        tags = jsonData["tags"]
        correctoutput = jsonData["correctoutput"]
        
        problemcode = jsonData["problemcode"]

        newproblem = Problem.objects.create(title=title, description=description, difficulty=difficulty, score=score, problemcode=problemcode, correctoutput=correctoutput)

        if newproblem.pk is not None:
            return JsonResponse({'status':'Problem Created Successfully'}, status=200)
        else:
          return JsonResponse({'status':'Problem Creation Failed from create method'}, status=400)
        
    except Exception as e: 

        return JsonResponse({'status':'Create Problem EXCEPTION OCCURED', 'exception':str(e)}, status=400)
