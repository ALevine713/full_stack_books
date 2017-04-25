from django.shortcuts import render, HttpResponse, redirect
from .models import Books

# Create your views here.
def index(request):
    context = {
    "books": Books.objects.all()
    }
    return render(request, "books/index.html", context)

def add_book(request):
    Books.objects.create(title=request.POST['title'], author=request.POST['author'], category=request.POST['category'])
    return redirect('/')
