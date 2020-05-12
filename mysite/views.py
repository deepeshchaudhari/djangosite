''''
    I have created this file
    Deepesh Chaudhari
'''
from django.http import HttpResponse
from  django.shortcuts import render
def  index(request):
    return render(request,'index.html')

def  about(request):
    return render(request,'about.html')

def  analyze(request):
    # get and analyze the text
    djtext = request.GET.get('text','default')
    # checknox value
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    encr = request.GET.get('encrypt','off')

    punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789'''
    analyzed =''
    purpose =''
    encrypted='Not Needed!!!'
    if removepunc == 'on':
        purpose ="Punctuation Removal"
        for char in djtext:
            if char not in punctuation:
                analyzed+=char
        djtext = analyzed
    if encr == 'on':
        print(djtext)
        encrypted =encrypt(djtext.lower(),4).replace('$',' ')
    if  fullcaps=='on':
        purpose = purpose+ " Capital letter"
        djtext = djtext.upper()
    # set to variable and send to html page
    param ={'purpose': purpose ,'analyzing': djtext,'encrypted':encrypted}
    return render(request,'analyze.html',param)

def  readtext(request):
    with open('E:/IIT KANPUR CSE/djangotuts/mysite/mysite/commands.txt') as f:
        data = f.read()
    params = {'data':data}
    return render(request,'readtext.html',params)

def encrypt(string,key):
    for x in string:
        if ord(x)>=123 or ord(x)< 97 and x!=' ':
            return "Punctuations are not removed!!!"
    res=''
    for x in string:
        if (ord(x)) % 2:
            if ord(x)- key< 97:res+=chr(ord(x)- key+26)
            else:res+=chr(ord(x)- key)
        else:
            if ord(x)+ key>122:res+=chr(ord(x) + key-26)
            else:res+=chr(ord(x) + key)
    return res