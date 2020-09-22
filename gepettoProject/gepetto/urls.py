from django.contrib import admin
from django.urls import path
import sttApp.views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sttApp.views.main),
    path('result/', sttApp.views.result, name='result'),
]
