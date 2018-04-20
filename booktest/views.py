from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.db.models import Max,F

from .models import *



# def index(request):
#
#
#     #list = BookInfo.books1.filter(heroinfo__hcontent__contains='八')
#     Max1 = BookInfo.books1.aggregate(Max('bpub_date'))
#
#     list = BookInfo.books1.filter(bread__gt=F('bcommet'))
#     content = {'list':list,
#                'Max1':Max1}
#
#     return render(request,'booktest/index.html',content)


def index(request):
    hero = HeroInfo.objects.get(pk=1)
    list = HeroInfo.objects.filter(isDelete=False)
    context={'list':list}
    return render(request,'booktest/index.html',context)


def show(request,id):
    context = {'id':id}

    return render(request,'booktest/show.html',context)


def index2(request):
    return render(request,'booktest/index2.html')

def user1(request):
    return render(request,'booktest/user1.html')

#html转义
def htmlTest(request):

    context = {'t1':'<h1>123</h1>'}
    return render(request,'booktest/htmlTest.html',context)

#跨站请求
def csrf1(request):
    return render(request,'booktest/csrf1.html')
def csrf2(request):
    uname=request.POST['uname']
    return HttpResponse(uname)