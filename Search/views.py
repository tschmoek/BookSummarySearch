from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from django import forms
from Search.Utils.AllUtils import AllUtils

def index(request):
	return HttpResponseRedirect('/search')

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():

            searchval = form.cleaned_data['searchval']
            return HttpResponseRedirect('/search')
    else:
    	form = SearchForm()
        
    return render(request, 'search.html', {'form': form})


class SearchForm(forms.Form):
    searchval = forms.CharField(label='Search', max_length=10000)

def searchQuery(request, query):
    # Data validation and everything is done in there..
    results = AllUtils.getAllSummeries(query)
    return JsonResponse(results)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)