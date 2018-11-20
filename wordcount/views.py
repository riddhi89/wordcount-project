from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter


def home(request):
    return render(request, 'home.html')

def count(request):
	fulltext = request.GET['fulltext']
	wordlist = fulltext.split()
	word_map = Counter(wordlist)

	return render(
		request, 'count.html',
		{
			'fulltext': fulltext,
			'count': len(wordlist),
			'sorted_word_map': sorted(word_map.items(), key=lambda x:x[1], reverse=True)
		}
	)

def about(request):
	return render(request, 'about.html')
