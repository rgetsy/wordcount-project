from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage (request):    #was home
    return render(request,'home.html')
def egg (request):
    return HttpResponse('I love eggs')
def about(request):
    return render(request, 'about.html')
def count (request):
    fulltext = request.GET['fulltext']
       ##returns info typed in text box
 ##   print(fulltext)
    wordlist = fulltext.split()       ##seperates words

    worddictionary={}

    for word in wordlist:
        if word in worddictionary:
            #increase count
            worddictionary[word] +=1
        else:
            #add to the dictionary
            worddictionary[word] =1
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})
