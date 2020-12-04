from django.shortcuts import render, redirect
from .models import Test
from mainApp.models import User
import os, sys
import random, copy
import requests

def input(request):
    return render(request, 'input.html')

def loading(request):
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
        response= requests.post(URL, data=data, headers=headers)
        rescode= response.status_code

        if(rescode== 200):
            response= response.text
        else:
            response = "Error : " + response.text
        
        test.text = response[9:-2]
        test.save()

        return render(request, 'loading.html', {'test':test})

def check(request, test_id):
    test = Test.objects.get(pk = test_id)
    return render(request, 'check.html', {'test':test})

def question(request, test_id):
    if 'modified_statement' in request.POST:
        test = Test.objects.get(pk = test_id)
        test.text = request.POST['modified_statement']
        test.save()

    mytest = Test.objects.get(pk = test_id)
    myStatement = mytest.text
    dataClass = data()
    originalStatement = dataClass.splitMystatement(myStatement)
    mytest.question1 = dataClass.makeQuestion1(originalStatement)[0]
    mytest.question2 = dataClass.makeQuestion2(originalStatement)[0]
    mytest.question3 = dataClass.makeQuestion3(originalStatement)[0]
    mytest.save()

    return render(request, 'question.html', {'mytest':mytest})

def result(request, test_id):
    if request.method == 'POST':
        incorrect_number = 0

        answer1 = request.POST['ox1']
        answer2 = request.POST['ox2']
        answer3 = request.POST['ox3']

        test = Test.objects.get(pk=test_id)
        test.answer1 = answer1
        test.answer2 = answer2
        test.answer3 = answer3

        if (test.text != test.question1) and (answer1 == 'O'):
            incorrect_number += 1
        if (test.text != test.question2) and (answer2 == 'O'):
            incorrect_number += 1
        if (test.text != test.question3) and (answer3 == 'O'):
            incorrect_number += 1
        
        test.test_probability = 100*(round(incorrect_number/3, 2))
        test.save()

        myStatement = test.text
        dataClass = data()
        originalStatement = dataClass.splitMystatement(myStatement)

        q1 = dataClass.splitMystatement(test.question1)
        q2 = dataClass.splitMystatement(test.question2)
        q3 = dataClass.splitMystatement(test.question3)


        q_when = q1[1]
        q_together = q2[3]
        q_what = q3[4]

        q_look1 = dataClass.resultLook1(test.question1, q_when)
        q_look2 = dataClass.resultLook2(test.question2, q_together)
        q_look3 = dataClass.resultLook3(test.question3, q_what)

    return render(request, 'result.html', {'test':test, 'q_when':q_when, 'q_together':q_together, 'q_what':q_what, 'q_look1':q_look1, 'q_look2':q_look2, 'q_look3':q_look3})

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
        r_unit = statement.split()

        for word in r_unit:
            if ("은" in word) or ("는" in word) or ("이" in word) or ("가" in word):
                who = word
                r_unit.remove(word)
                break

        for word in r_unit:
            if ("에서" in word) or ("서" in word):
                where = word
                r_unit.remove(word)
                break
        
        for word in r_unit:
            if ("와" in word) or ("과" in word) or ("랑" in word) or ("혼자" in word):
                together = word
                r_unit.remove(word)
                break

        for word in r_unit:
            if ("제" in word) or ("께" in word) or ("에" in word) or ("일" in word):
                when_index = r_unit.index(word)
            elif ("요" in word) or ("다" in word):
                what_index = r_unit.index(word)

        if (when_index < what_index):
            when = ' '.join(r_unit[:when_index+1])
            what = ' '.join(r_unit[when_index+1:])
        else:
            when = ' '.join(r_unit[what_index+1:])
            what = ' '.join(r_unit[:what_index+1])

        mystatement = [who, when, where, together, what]
        return mystatement
    
    def makeQuestion1(self, mystatement):
        question1 = copy.deepcopy(mystatement)
        random_when = random.choice(when_list)
        question1[1] = random_when
        question1 = [" ".join(question1),random_when]
        return question1
    
    def makeQuestion2(self, mystatement):
        question2 = copy.deepcopy(mystatement)
        random_together = random.choice(together_list)
        question2[3] = random_together
        question2 = [" ".join(question2), random_together]
        return question2
    
    def makeQuestion3(self, mystatement):
        question3 = copy.deepcopy(mystatement)
        random_what = random.choice(what_list)
        question3[4] = random_what
        question3 = [" ".join(question3), random_what]
        return question3

    def resultLook1(self, question1, q_when):
        result1 = copy.deepcopy(question1)
        splitResult1 = result1.split(q_when)
        return splitResult1
    
    def resultLook2(self, question2, q_together):
        result2 = copy.deepcopy(question2)
        splitResult2 = result2.split(q_together)
        return splitResult2

    def resultLook3(self, question3, q_what):
        result3 = copy.deepcopy(question3)
        splitResult3 = result3.split(q_what)
        return splitResult3
