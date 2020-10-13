from django.contrib import admin
from django.urls import path, include
import testApp.urls
import mainApp.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',include(mainApp.urls)),
    path('',include('testApp.urls')),
]
