from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """ 各地域の質問を表示する。"""
        return Question.objects.all()


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """ 公開日が現在より前の質問だけを表示させる。"""
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    

def vote(request, question_id):
    """ 投票数のインクリメントを行う。 """
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "選択肢を選んでください。",
        })
    else:
        now = timezone.now()
        if not question.was_published_recently(): 
            return timeInitialize(question, selected_choice, now)
        
        selected_choice.votes += 1
        selected_choice.save()
        
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    
    
def timeInitialize(question, selected_choice, now):
    """ 0時に票数を初期化する。 """
    today = str(now).split('-')
    pub_day = str(question.pub_date).split('-')
    day = int(today[2][:2])
    pday = int(pub_day[2][:2])
    question.pub_date += timezone.timedelta(days=day-pday)
    question.save()
        
    for choice in question.choice_set.all():
        if choice == selected_choice:
            choice.votes = 1
        else:
            choice.votes = 0
        choice.save()
    
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))