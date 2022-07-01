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
    try:

        # Only POST Method is accepted
        if(request.method!="POST"):
            return JsonResponse({'status':'Invalid Method'})


        if(not(request.user.is_authenticated)):
            return JsonResponse({'status':'User Authentication is required, which is not provided'}, status=400)

        if(not("problemcode" in request.headers and 
            
            "code-language" in request.headers)):

            return JsonResponse({'status':'Required Fields are missing in Create Problem API'}, status=400)

            
        
        user_id = request.user.id
        problemcode = request.headers["problemcode"]
        usercode=request.body.decode("utf-8")
        language=request.headers["code-language"]


        # newsubmission = Submission(user_id=user, problem_id=problem, usercode=userc)
        cppfilename = str(user_id)+"_"+str(problemcode)+"_code.cpp";
        f = open(cppfilename, "w")
        f.write(usercode)
        f.close()
        
        
        tmpcompile = sb.run("g++ "+cppfilename, shell=True,stdout=sb.PIPE, stderr=sb.PIPE)
        # if(tmpcompile.returncode != 0):
        #     return JsonResponse({'status':tmpcompile.stderr}, status=401)

        print("COMPILED")
        if(tmpcompile.returncode == 0):

            print("CHECKING")

            problemstdin= open("in.txt","r")
            tmpuseroutput = sb.run("./a.out",stdout=sb.PIPE, stderr=sb.PIPE, stdin=problemstdin)
            problemstdin.close()
        

            print("COMPILED")
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
            
            f = open(str('files_usersubmissions/'+str(newSubmission.id)+'.txt'), "w")
            f.write(useroutput)
            f.close()


            
            if os.path.exists(cppfilename):
                os.remove(cppfilename)

            

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

            f = open(str('files_usersubmissions/'+str(newSubmission.id)+'.txt'), "w")
            f.write(useroutput.decode("utf-8"))
            f.close()

            return JsonResponse({
                'verdict':verdict,
                'status' : status,   
                'submission':str(model_to_dict(newSubmission))
            })

    except Exception as e: 
        return JsonResponse({'status':'getProfile EXCEPTION OCCURED', 'exception':str(e)}, status=400)
