from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse

from .models import Post
from django.shortcuts import get_object_or_404
# Create your views here.
#def posthome(request):
#	return HttpResponse("<h1>Айболит и его друзья</h1>")



def posthome(request):
	return render(request, "index.html",())

def postcreate(request):
	return HttpResponse("<h1>Создание</h1>")

def postdetail(request):
	return HttpResponse("<h1>Рассказ целиком</h1>")

def postlist(request):
	return HttpResponse("<h1>Список рассказов</h1>")

def postupdate(request):
	return HttpResponse("<h1>Редактирование рассказа</h1>")

def postdelete(request):
	return HttpResponse("<h1>Удаление рассказа</h1>")

def bookshome(request):
	content={"title":"Домашняя страница книг"}
	return render(request,"index.html",content)

def bookscreate(request):
	content={"title":"Создание книги"}
	return render(request,"index.html",content)
	#return render(request,"index.html",{"title":"Создание книги"})

def booksdetail(request,id=None):
	#instance=Post.objects.get(id=2)
	instance=get_object_or_404(Post,id=id)
	content={
		"title":instance.title,
		"instance":instance,
		}
	return render(request,"booksdetail.html",content)

def bookslist(request):
	querybook=Post.objects.all
	content={
		"title":"Список книг",
		"object_list":querybook,
		}
	#return HttpResponse("<h1>Список книг</h1>")
	return render(request,"index.html",content)

def booksupdate(request):
	content={"title":"Обновление книги"}
	return render(request,"index.html",content)

def booksdelete(request):
	content={"title":"Удаление книги"}
	return render(request,"index.html",content)
