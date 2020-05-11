''''
    I have created this file
    Deepesh Chaudhari
'''
from django.http import HttpResponse
from  django.shortcuts import render
def  index(request):
    # params = {'name': 'Deepesh Chaudhari', 'place': 'Kanpur'}
    return render(request,'index.html')

def  about(request):
    return render(request,'about.html')

def  analyze(request):
    # get and analyze the text
    djtext = request.GET.get('text','default')
    # checknox value
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')

    punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789'''
    analyzed =''
    purpose =''
    # apply operation according to checkbos value
    if removepunc =='on' and fullcaps=='off':
        purpose ="Punctuation Removal"
        for char in djtext:
            if char not in punctuation:
                analyzed+=char
        print(analyzed)
    elif removepunc =='on' and fullcaps=='on':
        purpose ="Punctuation Removal and change to uppercase"
        for char in djtext:
            if char not in punctuation:
                analyzed+=char
        analyzed = analyzed.upper()
    elif removepunc =='off' and fullcaps=='on':
        purpose ="Change to uppercase"
        analyzed = djtext.upper()
    else:
        analyzed=djtext

    # set to variable and send to html page
    param ={'purpose': purpose ,'analyzing': analyzed}
    return render(request,'analyze.html',param)

def  readtext(request):
    with open('E:/IIT KANPUR CSE/djangotuts/mysite/mysite/commands.txt') as f:
        data = f.read()
    params = {'data':data}
    return render(request,'readtext.html',params)