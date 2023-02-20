from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.template import loader
from .models import Choice, Suggestion
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_suggestion_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Suggestion.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Suggestion
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Suggestion.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Suggestion
    template_name = 'polls/results.html'

    # def results(request, suggestion_id):
    #     suggestion = get_object_or_404(Suggestion, pk=suggestion_id)
    #     return render(request, 'polls/results.html', {'suggestion': suggestion})

def vote(request, suggestion_id):
    suggestion = get_object_or_404(Suggestion, pk=suggestion_id)
    try:
        selected_choice = suggestion.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the suggestion voting form.
        return render(request, 'polls/detail.html', {
            'suggestion': suggestion,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('feedback:results', args=(suggestion.id,)))
