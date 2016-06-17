
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone


from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'poll/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        """Return the last five published question"""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
        
class DetailView(generic.DetailView):
    model = Question
    template_name = 'poll/detail.html'
    
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())
    
    
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'poll/results.html'

    
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        #Redisplay the question voting form
        return render(request, 'poll/detail.html', {
        'question': question,
        'error_message': "You didnt select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('poll:results', args=(question.id,)))

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'poll/detail.html', {'question': question})