from django.http import HttpResponseRedirect
from django.shortcuts import render
from blogapp.models import Archives, Comments


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

def comment(request):
    archid = request.REQUEST.get('id')
    author = request.REQUEST.get('author')
    content = request.REQUEST.get('content')
    email = request.REQUEST.get('email')
    link = request.REQUEST.get('link')
    arch = Archives.objects.get(id=archid)
    #foolish method to validate,will be improved soon.
    if author != '' and content != '' and email != '':
        p = Comments.objects.create(archiveid=arch, author=author, email=email, content=content, archivetitle=arch.title, link=link)
        return HttpResponseRedirect('/%d'%arch.id)
    else:
        return HttpResponseRedirect('/%d'%arch.id)