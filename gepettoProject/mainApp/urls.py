from django.urls import path
import mainApp.views 

urlpatterns = [
    path('', mainApp.views.main, name='main'),
    path('login/', mainApp.views.LoginView.as_view(), name='login'),
    path('logout/', mainApp.views.Logout, name='logout'),
    path('signup/', mainApp.views.SignupView.as_view(), name='signup'),
    path('mypage/', mainApp.views.mypage, name='mypage'),
    path('mypage-edit/', mainApp.views.mypage_edit,name='mypage_edit'),
    path('logout/', mainApp.views.logout, name='logout'),
]