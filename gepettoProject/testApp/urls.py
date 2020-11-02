from django.urls import path
import testApp.views 

urlpatterns = [
    path('', testApp.views.input, name='input'),
    path('check/', testApp.views.check, name='check'),
    path('question/', testApp.views.question, name='question'),
    path('result/', testApp.views.result, name='result'),
]
