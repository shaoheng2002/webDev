from django.shortcuts import render, reverse
from django.http import HttpResponse
from _datetime import datetime
from django.db import connection


# Create your views here.
def index(request):
    cursor = connection.cursor()
    # cursor.execute('insert into website value `shao`,`www.shao.com`,`123`,`USA`')
    cursor.execute('select name from website')
    rows = cursor.fetchall()
    print (rows)
    website = [row[0] for row in rows]
    list = [i for i in range(10)]
    text={
            'text':"This is the text from parameter",
            'age':14,
            'list':list,
            'date':datetime.now(),
            'websites':website,
          }
    return render(request, 'index.html', context=text)

def url(request):
    return render(request, 'url.html')

def read(request):
    return HttpResponse("Read")

def movie(request):
    return HttpResponse("movie")

def find(request):
    return HttpResponse("find")