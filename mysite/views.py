''''
    I have created this file
    Deepesh Chaudhari
'''
from django.http import HttpResponse
def  index(request):
    return HttpResponse("<h1>yeah! this is first Django site</h1>")
def  about(request):
    return HttpResponse("This is about Django page")
def  readtext(request):
    with open('E:/IIT KANPUR CSE/djangotuts/mysite/mysite/commands.txt') as f:
        data = f.read()
        return HttpResponse(data)