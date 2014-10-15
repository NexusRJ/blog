from django.http import HttpResponseRedirect
from django.shortcuts import render
from blogapp.models import Archives, Comments
#How many archives must a page show?
onepage = 3


def archive(request):
    #pageinator
    try:
        curpage = int(request.GET.get('curPage', 1))
        allpage = int(request.GET.get('allPage', 1))
        pagetype = str(request.GET.get('pageType', ''))
    except ValueError:
        curpage = 1
        allpage = 1
        pagetype = ''
    #just calculate once when first connect db
    if curpage == 1 and allpage == 1:
        allpagecounts = Archives.objects.count()
        allpage = allpagecounts/onepage
        remainpages = allpagecounts % onepage
        if remainpages > 0:
            allpage += 1
    if pagetype == 'pageUp':
        curpage -= 1
    elif pagetype == 'pageDown':
        curpage += 1
    startpage = (curpage-1) * onepage
    endpage = startpage + onepage
    archives = Archives.objects.all()[startpage:endpage]
    return render(request, 'archive.html', {'archives': archives, 'curPage': curpage, 'allPage': allpage})


def showblog(request, name):
    thisblog = Archives.objects.get(id=name)
    thiscomment = thisblog.comments_set.all()
    return render(request, 'showblog.html', {'thisblog': thisblog, 'thiscomment': thiscomment,})


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