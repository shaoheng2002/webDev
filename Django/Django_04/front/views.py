from django.shortcuts import render, reverse, redirect
from django.db import connection
from django.http import HttpResponse

def get_cursor():
    return connection.cursor()
# Create your views here.
def index(request):
    cursor = get_cursor()
    cursor.execute("select id, name, author from book")
    books = cursor.fetchall()
    return render(request, 'index.html', context={'books':books})

def add_book(request):
    if request.method=='GET':
        return render(request, 'add_book.html')
    else:
        name = request.POST.get('name')
        author =request.POST.get('author')
        cursor = get_cursor()
        cursor.execute("insert into book (id, name, author) value (null, '%s', '%s')" % (name, author))
        return redirect(reverse('index'))

def book_detail(request, book_id):
    cursor = get_cursor()
    cursor.execute("select id, name, author from book where id = %s" % book_id)
    book = cursor.fetchone()
    return render(request, 'book_detail.html', context={'book':book})

def delete_book(request):
    if request.method=='POST':
        book_id=request.POST.get('book_id')
        cursor = get_cursor()
        cursor.execute("delete from book where id = %s" % book_id)
        return redirect(reverse('index'))
    else:
        return HttpResponse("删除错误！ Not a POST request")



