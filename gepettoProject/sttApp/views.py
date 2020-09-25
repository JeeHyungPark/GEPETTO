from django.shortcuts import render
import os, sys
import requests


def main(request):
    return render(request, 'main.html')

def result(request):
   
    file_path= 'sttApp/test.mp3' #추후 request.POST['data'] 로 변경해야 함(media)
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

    return render(request, 'result.html', {'response':response})
