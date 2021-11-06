from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.urls import reverse


def index(request):
    return render(request, 'first.html')

def about(request):
    return render(request, 'about.html')

def index1(request, urlDate):
    result = urlDate + 1
    result = str(result)
    return HttpResponse("这是我的第一个Django页面" + result)

def index2(request, data):
    return HttpResponse("这是我的第一个Django页面" + data)

def index3(request, data, age):
    return HttpResponse("URL：" + data + "，附加数据" + age)

def index4(request, data="100"):
    return HttpResponse("default：100" + "，url:" + data)

def student_1801(request):
    return HttpResponse("hello!!!")

def student(request, year):
    return HttpResponse("Year: " + year)

def student1(request, year, month):
    return HttpResponse("Year: " + year + ", mouth:" + month)

def jiexi(request):
    return HttpResponse("请求的url是：" + reverse('jiexi1'))

def jiexi2(request, data):
    return HttpResponse("请求的url是：" + reverse('jiexi2', args=[data]))

def reverserTemplate(request, data):
    return render(request, 'showUrl.html', {'data': data})