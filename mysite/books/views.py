from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django import forms
from books.models import Author,Book
from django.shortcuts import render_to_response


def hello(request):
    return render_to_response('hello.html')
    
def index(request):
    return render_to_response('index.html')
    
    
def add(request):
    book_list = Book()
    if request.POST:
        book_list.ISBN = request.POST['ISBN']
        book_list.Title = request.POST['Title']
        book_list.AuthorID = request.POST['AuthorID']
        book_list.Publisher = request.POST['Publisher']
        book_list.PublishDate = request.POST['PublishDate']
        book_list.Price = request.POST['Price']
        author_id = book_list.AuthorID
        book_list.save()
        try:
            author = Author.objects.get(AuthorID = author_id)
            return render_to_response('add_Successed.html')
        except:     
            return render(request,'needauthor.html')
    else:
        return render(request,'add.html')
        
def addauthor(request):
    author_list = Author()
    if request.POST:
        author_list.Name = request.POST['Name']
        author_list.AuthorID = request.POST['AuthorID']
        author_list.Age = request.POST['Age']
        author_list.Country = request.POST['Country']
        author_list.save()
        author_id = author_list.AuthorID
    try:
         author = Author.objects.get(AuthorID = author_id)
         return render_to_response('add_Successed.html')
    except:     
         return render(request,'addauthor.html',{'author':author_list})  
def add_Successed(request):
    return render_to_response('add_successed.html')

def detailedbook(request):
    if 'ISBN' in request.GET:
        book=Book.objects.get(ISBN = request.GET['ISBN'])
        author_id = book.AuthorID
        author = Author.objects.get(AuthorID = author_id)
    return render_to_response('detail.html',{'book':book , 
                                             'author': author })
                                             
def updata(request):
    if 'ISBN' in request.GET:
        book_list = Book.objects.get(ISBN = request.GET['ISBN'])
        authorid = book_list.AuthorID
        author_list = Author.objects.get(AuthorID = authorid)
    if request.POST:
        book_list.ISBN = request.POST['ISBN']
        book_list.Title = request.POST['Title']
        book_list.Publisher = request.POST['Publisher']
        book_list.PublishDate = request.POST['PublishDate']
        book_list.Price = request.POST['Price']
        author_list.Name = request.POST['Name']
        author_list.Age = request.POST['Age']
        author_list.Country = request.POST['Country']  
        author_id = book_list.AuthorID
        book_list.save()
        author_list.save()
    try:

         author = Author.objects.get(AuthorID = author_id)
         return render_to_response('updata_Successed.html')
    except:     
        return render_to_response('updata.html',{'book':book_list , 
                                             'author': author_list })  
def updata_Successed(request):
    return render_to_response('updata_Successed.html')
    
def delete(request):
    if 'ISBN' in request.GET:
        n_book_lst = Book.objects.get(ISBN = request.GET['ISBN'])
        n_book_lst.delete()
    book_lst = Book.objects.all()
    return render_to_response('show.html', {'book_lst': book_lst})
    
    
def show(request):
    book_lst = Book.objects.all()
    return render_to_response('show.html', {'book_lst':book_lst})
    
    
def search_form(request):
  return render_to_response('search.html') 
  
def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        try:
            author = Author.objects.get(Name = q)
            bookid = author.AuthorID
            book = Book.objects.filter(AuthorID = bookid)
            return render_to_response('search_results.html',
                       {'author': author, 'query': q,'book': book})
        except:
            return render_to_response('search_again.html')
    else:
        return render_to_response('search.html')

def search_again(request):
    return render_to_response('search_again.html')



