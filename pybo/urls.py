from django.urls import path
from . import views

app_name = 'pybo'

# path 끝에 comma(,) 잊지 말기
urlpatterns = [
    path('', views.index, name='index'), # config\urls.py에 이미 'pybo/'가 존재함 -> ''로만 써도 열림
    path('<int:question_id>/', views.detail, name='detail'), # '정수형:질문 ID/'로 된 URL을 views.py의 detail 함수에 매핑
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
]