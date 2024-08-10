from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer
from django.http import HttpResponseNotAllowed
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    """
    pybo 목록 출력
    """
    # 입력 인자
    page = request.GET.get('page', '1')    # 1페이지 가져와서 페이지(page) 객체를 만듬
    # 조회
    question_list = Question.objects.order_by('-create_date')
    # 페이징 처리
    paginator = Paginator(question_list, 10)   # 전체 question_list를 10개씩 묶어서 각 페이지로 만들기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}     # question_list는 페이징 객체(page_obj)임
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":            #POST 방식이라면,
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:                                   # GET 방식이면(POST 방식이 아니라면)
        return HttpResponseNotAllowed('Only POST is possible.')   # ‘POST만 가능합니다' 오류 발생
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

def question_create(request):
    if request.method == 'POST': # 요청이 POST 방식이면
        form = QuestionForm(request.POST)
        if form.is_valid():  # 폼이 유효하다면
            question = form.save(commit=False)  # 임시 저장하여 question 객체를 리턴받는다.
            question.create_date = timezone.now()  # 실제 저장을 위해 작성일시를 설정한다.
            question.save()  # 데이터를 실제로 저장한다.
            return redirect('pybo:index') # pybo:index로 이동함, 실 주소는 localhost:8000/pybo/
    else:                       # 요청이 POST 방식이 아니면 (GET 방식이면)
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)
