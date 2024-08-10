from django.urls import path
from django.contrib.auth import views as auth_views # django.contrib.auth 앱 views 파일의 별명
from . import views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'), #이 링크의 별명은 'login'
    #django.contrib.auth 앱 views 파일의 LoginView 클래스의 as_view() 함수 사용
    path('logout/', views.logout_view, name='logout'),
]