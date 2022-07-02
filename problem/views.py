import os
import json
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from .models import Problem, Testcase


def create_problem(request):
    try:
        if(request.method != "POST"):
            return JsonResponse({'status':'Invalid create_problem Method'}, status=400)
        

        jsonData = json.loads(request.body)

        if(not("title" in jsonData and "description" in jsonData and "difficulty" in jsonData and "score" in jsonData and "tags" in jsonData and "problemcode" in jsonData and "correctoutput" in jsonData and "testcases" in jsonData)):
            return JsonResponse({'status':'Required Fields are missing in Create Problem API'}, status=400)

        title = jsonData["title"]
        description = jsonData["description"]
        difficulty = jsonData["difficulty"]
        score = jsonData["score"]
        tags = jsonData["tags"]
        correctoutput = jsonData["correctoutput"]
        
        testcases = jsonData["testcases"]
        
        problemcode = jsonData["problemcode"]


        # Creating Problem Instance in Database

        newproblem = Problem.objects.create(title=title, description=description, difficulty=difficulty, score=score, problemcode=problemcode)


        # Directory path of problem 
        testcasesPath = "files_testcases/"+str(problemcode)

        print(testcasesPath)
        if(not os.path.exists(testcasesPath)):
            os.makedirs(testcasesPath)

        # for checking if given object is List or not
        if not isinstance(testcases, list):
            return JsonResponse({'status':'Invalid Testcases type'}, status=400)
        
        # Checking if all the keys are present in object or not
        for testcaseIndex,eachTestcase in enumerate(testcases):
            if(not(("input" in eachTestcase and "output" in eachTestcase))):
                return JsonResponse({'status':'Properties missing from testcases'}, status=400)
        

        # testcases file paths in list
        testcasesFilePathInList = []


        # Checking if all the keys are present in object or not
        for testcaseIndex,eachTestcase in enumerate(testcases):

            
            # creating directory if not exists
            if(not os.path.exists(testcasesPath+"/"+str(testcaseIndex))):
                os.makedirs(testcasesPath+"/"+str(testcaseIndex))
            
            # creating input and output files
            testcaseInputFilePath = testcasesPath+"/"+str(testcaseIndex)+"/input.txt"
            testcaseOutputFilePath = testcasesPath+"/"+str(testcaseIndex)+"/output.txt"


            fileHandler = open(testcaseInputFilePath,"w")
            fileHandler.write(eachTestcase["input"])
            fileHandler.close()

            fileHandler = open(testcaseOutputFilePath,"w")
            fileHandler.write(eachTestcase["output"])
            fileHandler.close()

            newTmptestcase = Testcase.objects.create(
                title=problemcode+'_testcase_'+str(testcaseIndex),
                input_path = testcaseInputFilePath, 
                output_path=testcaseOutputFilePath,
                problem_id = newproblem.id
                )

            # testcasesFilePathInList.append({'input':testcaseInputFilePath, 'output':testcaseOutputFilePath}) 

        # Storing Paths of Input & Output Files in Databases to reachout those files during problem submissions and testcase against user submissions
        newproblem.testcasesinputandoutput = str(testcasesFilePathInList)
        newproblem.save()




        if newproblem.pk is not None:
            return JsonResponse({'status':'Problem Created Successfully'}, status=200)
        else:
          return JsonResponse({'status':'Problem Creation Failed from create method'}, status=400)
        
    except Exception as e: 

        return JsonResponse({'status':'Create Problem EXCEPTION OCCURED', 'exception':str(e)}, status=400)
