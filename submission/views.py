from os import stat
import os
import subprocess as sb
import json
from sys import stdout
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict


from .models import Submission
from problem.models import Problem
def create_submission(request):

    # Only POST Method is accepted
    if(request.method!="POST"):
        return JsonResponse({'status':'Invalid Method'})


    if(not(request.user.is_authenticated)):
        return JsonResponse({'status':'User Authentication is required, which is not provided'}, status=400)

    jsonData = json.loads(request.body)
    if(not("problemcode" in jsonData and 
           "usercode" in jsonData and
           "language" in jsonData)):

           return JsonResponse({'status':'Required Fields are missing in Create Problem API'}, status=400)
    
    user_id = request.user.id
    problemcode = jsonData["problemcode"]
    usercode=jsonData["usercode"]
    language=jsonData["language"]



    # newsubmission = Submission(user_id=user, problem_id=problem, usercode=userc)

    f = open("code.cpp", "w")
    f.write(usercode)
    f.close()

    tmpcompile = sb.run("g++ code.cpp", shell=True,stdout=sb.PIPE, stderr=sb.PIPE)

    # if(tmpcompile.returncode != 0):
    #     return JsonResponse({'status':tmpcompile.stderr}, status=401)
    if(tmpcompile.returncode == 0):

        tmpuseroutput = sb.run("./a.out",stdout=sb.PIPE, stderr=sb.PIPE)

        print('sdf')
        problemobj = Problem.objects.get(problemcode=(problemcode))
        
        score = problemobj.score
        correctoutput = problemobj.correctoutput

        print(correctoutput.split())


        useroutput = tmpuseroutput.stdout
        useroutput = useroutput.decode('unicode_escape')
        print(str(useroutput).split())


        if(correctoutput.split() == str(useroutput).split()):
            verdict = "ACCEPTED";
            status = "SUBMITTED"    

        else:
            verdict = "WRONG ANSWER"
            status = "SUBMITTED"

        

        # if(tmpuseroutput.returncode != 0):
        #     return JsonResponse({'status':tmpcompile.stderr}, status=401)


        submissionTime = "submissionTime"
        

        newSubmission = Submission.objects.create(problem_id=problemobj.id, user_id=user_id, usercode=usercode, useroutput=useroutput, verdict=verdict, language=language, status=status, score=score)


        print(newSubmission)
        

        if os.path.exists("code.cpp"):
            os.remove("code.cpp")

        

        if os.path.exists("a.out"):
            os.remove("a.out")
        return JsonResponse({
            'verdict':verdict,
            'status' : status,    
            'submission':str(model_to_dict(newSubmission))
        })

    else:
        useroutput = tmpcompile.stderr
        verdict = "COMPILATION ERROR"
        status = "COMPILATION ERRROR"
        problemobj = Problem.objects.get(problemcode=problemcode)
        score = problemobj.score

        newSubmission = Submission.objects.create(problem_id=problemobj.id, user_id=user_id, usercode=usercode, useroutput=useroutput, verdict=verdict, language=language, status=status, score=score)

        return JsonResponse({
            'verdict':verdict,
            'status' : status,   
            'submission':str(model_to_dict(newSubmission))
        })

  