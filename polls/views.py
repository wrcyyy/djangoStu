from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question


# Create your views here.

def index(request):
    context = {
        'latest_question_list': Question.objects.order_by('-pub_date')[:5]
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return render(request, 'polls/detail.html', {'question': get_object_or_404(Question, pk=question_id)})


def results(request, question_id):
    return HttpResponse(f'您正在查看问题结果：{question_id}')


def vote(request, question_id):
    return HttpResponse(f'您正在给问题{question_id}投票')
