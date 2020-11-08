from django.shortcuts import render, redirect
from .models import Test
from mainApp.models import User
import os, sys
import requests

def input(request):
    return render(request, 'input.html')

def check(request):
    
   if request.method == 'POST':
        test = Test.objects.create(
            tester = request.user,
            statement = request.FILES['statement']
        )

        file_path= 'testApp'+test.statement.url 
        data= open(file_path, "rb") # STT를 진행하고자 하는 음성 파일

        Lang= "Kor" # Kor / Jpn / Chn / Eng
        URL= "https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang=" + Lang
            
        ID= "lnm6jnyxaa" # 인증 정보의 Client ID
        Secret= "PcMs6ZXMVXpn4TZFDexuCe2S8k3BsCcYfWzgnJBD" # 인증 정보의 Client Secret
            
        headers= {
            "Content-Type": "application/octet-stream", # Fix
            "X-NCP-APIGW-API-KEY-ID": ID,
            "X-NCP-APIGW-API-KEY": Secret,
        }
        response= requests.post(URL,  data=data, headers=headers)
        rescode= response.status_code

        if(rescode== 200):
            response= response.text
        else:
            response = "Error : " + response.text
        
        test.text = response[9:-2]
        test.save()

        return render(request, 'check.html', {'response':response[9:-2], 'test':test})

def question(request, test_id):
    if request.method == 'POST':
        test = Test.objects.get(pk = test_id)
        test.text = request.POST['modified_statement']
        test.save()
        
    return render(request, 'question.html')

def result(request):
    return render(request, 'result.html')
