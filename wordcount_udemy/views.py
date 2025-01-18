from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordList = fulltext.split()
    
    wordRanking = {}
    for word in wordList:
        if word in wordRanking:
            #increase number 
            wordRanking[word] += 1

        else:
            #add the word
            wordRanking[word] = 1
    
    sortedWordRanking = sorted(wordRanking.items(), key=operator.itemgetter(1), reverse = True)

    return render(request, 'count.html', 
                  {"fulltextis": fulltext,
                   "wordcountis": len(wordList),
                   "wordrankingis": wordRanking.items,
                   "sortedWordRankingis":sortedWordRanking,
                   "sortedWordRankingtrunicated": sortedWordRanking[0:3],
                   })

def about(request):
    
    return render(request, 'about.html')
