''''
    I have created this file
    Deepesh Chaudhari
'''
from django.http import HttpResponse
from  django.shortcuts import render
def  index(request):
    return render(request,'index.html')

def  analyze(request):
    # get text value
    djtext = request.POST.get('text','default')

    # checknox value
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    encr = request.POST.get('encrypt','off')
    decr = request.POST.get('decrypt','off')
    all = request.POST.get('all','off')

    # initialize variable
    punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789'''
    analyzed =''
    purpose =''
    encrypted='Not Needed!!!'
    decrypted='Not Needed!!!'

    # operation according to value
    if decr=='on' or all=='on':
        decrypted = decrypt(djtext,4)

    if removepunc == 'on' or all=='on':
        purpose ="Punctuation Removal"
        for char in djtext:
            if char not in punctuation:
                analyzed+=char
        djtext = analyzed

    if encr == 'on' or all=='on':
        print(djtext)
        encrypted =encrypt(djtext.lower(),4).replace('$',' ')

    if  fullcaps=='on' or all=='on':
        purpose = purpose+ " Capital letter"
        djtext = djtext.upper()

    # set to variable and send to html page
    param ={'purpose': purpose ,'analyzing': djtext,'encrypted':encrypted,'decrypted':decrypted}
    return render(request,'analyze.html',param)

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

def decrypt(string,key):
    if not string:
        return False
    for x in string:
        if ord(x)>122 or ord(x)<97 and x!=' ':
            return False
    res=''
    if key%2==0:
        for x in string:
            if (ord(x)) % 2==0:
                if ord(x)- key< 97: res+=chr(ord(x)- key+26)
                else:  res+=chr(ord(x)- key)
            else:
                if ord(x)+ key>122: res+=chr(ord(x) + key-26)
                else:  res+=chr(ord(x) + key)
    else:
        for x in string:
            if (ord(x)) % 2:
                if ord(x)- key< 97: res+=chr(ord(x)- key+26)
                else:  res+=chr(ord(x)- key)
            else:
                if ord(x)+ key>122: res+=chr(ord(x) + key-26)
                else:  res+=chr(ord(x) + key)
    return res.replace('6',' ')