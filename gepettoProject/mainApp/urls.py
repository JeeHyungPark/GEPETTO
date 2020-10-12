from django.urls import path
import mainApp.views 

urlpatterns = [
    path('', mainApp.views.main),
    path('login/', mainApp.views.login, name='login'),
    path('signup/', mainApp.views.signup, name='signup'),
    path('mypage/', mainApp.views.mypage, name='mypage'),
    path('mypage-edit/', mainApp.views.mypage_edit,'mypage_edit'),
]