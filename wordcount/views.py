from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html',{'Hithere'  : 'It Me'})

def aboutus(request):
    return render(request,'aboutus.html')


def count(request):
    fulltext=request.GET['FullText']
    wordlist =fulltext.split()
    worddic={}
    for word in wordlist:
        if word in worddic:
            #Increase
            worddic[word] +=1


        else:
            worddic[word]=1


        sortedwords=sorted(worddic.items(),key=operator.itemgetter(1), reverse = True)

    return render(request,'count.html',{'FullText' : fulltext , 'Length':len(wordlist),'worddic':sortedwords})
