from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>This is the default Home page</h1>")


def book(request):
    return HttpResponse('Book - Homepage')

def book_detail(requiet, book_id):
    text="your book id is : %s" % book_id
    return HttpResponse(text)

def author_detail(request):
    author_id = request.GET.get('id') # input the /author/?id=""
    text="Author_ID of this book is : %s" % author_id
    return HttpResponse(text)