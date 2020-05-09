#coding=utf-8

from  django.http import  HttpResponse
def index_view(request):
    return HttpResonse('hello git!')