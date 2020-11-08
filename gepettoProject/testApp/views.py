from django.shortcuts import render, redirect
from .models import Test
from mainApp.models import User
import os, sys
import random, copy
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

        if 'modified_statement' in request.POST:
            test = Test.objects.get(pk = test_id)
            test.text = request.POST['modified_statement']
            test.save()

        mytest = Test.objects.get(pk = test_id)
        myStatement = mytest.text
        dataClass = data()
        originalStatement = dataClass.splitMystatement(myStatement)
        mytest.question1 = dataClass.makeQuestion1(originalStatement)
        mytest.question2 = dataClass.makeQuestion2(originalStatement)
        mytest.question3 = dataClass.makeQuestion3(originalStatement)
        mytest.save()

    return render(request, 'question.html')

def result(request):
    return render(request, 'result.html')

## 질문생성을 위함 ##
path_dir= '../dataset/'
file_list= os.listdir(path_dir) 
statement_list= []
who_list= []
when_list= []
where_list= []
together_list= []
what_list= []

for datafile in file_list: 
    f= open(path_dir+datafile, 'r')  
    statement= f.readline()
    unit= statement.split() 
    who= unit[0]  
    who_list.append(who) 
    
    for word in unit:
        if "에서" in word:
            where_list.append(word)
            where_index= unit.index(word)
            when= unit[1:where_index]
            when= ' '.join(when)
            when_list.append(when)
        if ("와" in word) or ("과" in word) or ("랑" in word) or ("혼자" in word):
            together_list.append(word)
            together_index= unit.index(word)
            what= unit[together_index+1:]
            what= ' '.join(what)
            what_list.append(what)

statement_list = [who_list, when_list, where_list, together_list, what_list]

class data:
    def splitMystatement(self,statement):
        unit = statement.split()
        who = unit[0]
        for word in unit:
            if "에서" in word:
                where = word
                where_index = unit.index(word)
                when = unit[1:where_index]
                when = ' '.join(when)
            if ("와" in word) or ("과" in word) or ("랑" in word) or ("혼자" in word):
                together = word
                together_index= unit.index(word)
                what = unit[together_index+1:]
                what = ' '.join(what)
        mystatement = [who, when, where, together, what]
        return mystatement
    
    def makeQuestion1(self, mystatement):
        question1 = copy.deepcopy(mystatement)
        random_when = random.choice(when_list)
        question1[1] = random_when
        question1 = " ".join(question1)
        return question1
    
    def makeQuestion2(self, mystatement):
        question2 = copy.deepcopy(mystatement)
        random_together = random.choice(together_list)
        question2[3] = random_together
        question2 = " ".join(question2)
        return question2
    
    def makeQuestion3(self, mystatement):
        question3 = copy.deepcopy(mystatement)
        random_what = random.choice(what_list)
        question3[4] = random_what
        question3 = " ".join(question3)
        return question3
