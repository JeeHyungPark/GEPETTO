from django.contrib import admin
from django.urls import path, include
import testApp.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/',include('testApp.urls')),
]
