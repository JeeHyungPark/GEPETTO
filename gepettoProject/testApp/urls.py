from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import testApp.views 

urlpatterns = [
    path('', testApp.views.input, name='input'),
    path('check/', testApp.views.check, name='check'),
    path('question/', testApp.views.question, name='question'),
    path('result/', testApp.views.result, name='result'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
