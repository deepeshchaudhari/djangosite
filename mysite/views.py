''''
    I have created this file
    Deepesh Chaudhari
'''
from django.http import HttpResponse
from  django.shortcuts import render
def  index(request):
    params = {'name': 'Deepesh Chaudhari', 'place': 'Kanpur'}
    return render(request,'index.html',params)
def  about(request):
    return render(request,'about.html')
def  readtext(request):
    with open('E:/IIT KANPUR CSE/djangotuts/mysite/mysite/commands.txt') as f:
        data = f.read()
    params = {'data':data}
    return render(request,'readtext.html',params)