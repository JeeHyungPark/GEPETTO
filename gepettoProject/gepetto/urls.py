from django.contrib import admin
from django.urls import path, include
import testApp.urls
import mainApp.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(mainApp.urls)),
    path('test/',include('testApp.urls')),
]
