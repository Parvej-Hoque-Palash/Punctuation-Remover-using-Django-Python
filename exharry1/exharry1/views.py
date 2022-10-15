from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'index.html')
def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    print(removepunc)
    print(djtext)
    #analyzed = djtext
    punctuations = '''!()-[]{}:;'"\,<>./?@#$%^^&*_~'''
    analyzed=""
    for char in djtext:
        if char not in punctuations:
            analyzed= analyzed + char

    params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
    return render(request,'analyze.html', params)

