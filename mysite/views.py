''''
    I have created this file
    Deepesh Chaudhari
'''
from django.http import HttpResponse
def  index(request):
    return HttpResponse("yeah! this is first Django site")