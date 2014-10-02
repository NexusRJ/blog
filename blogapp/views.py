from django.shortcuts import render
from blogapp.models import Archives


def archive(request):
    archives = Archives.objects.all()
    return render(request, 'archive.html', {'archives': archives,})


def showblog(request, name):
    thisblog = Archives.objects.get(id=name)
    return render(request, 'showblog.html', {'thisblog': thisblog,})


def books(request):
    archives = Archives.objects.all()
    return render(request, 'books.html', {'archives': archives})


def codes(request):

    archives = Archives.objects.all()
    return render(request, 'codes.html', {'archives': archives})


def about(request):
    return render(request,'about.html',{})