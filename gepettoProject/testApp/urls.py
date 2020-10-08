from django.urls import path
import testApp.views 

urlpatterns = [
    path('', testApp.views.input),
    path('result/', testApp.views.result, name='result'),
]
