from django.core.paginator import Paginator
from django.shortcuts import render

from post.models import Post


def home(request):
    blog = Post.objects.all()
    paginator = Paginator(blog,2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'home/home.html',{'blog':page_obj})
#chon ghablan baraye post ha az esme blog stefade karde boodim dg inja ham faght value ra tagheer dadim


def search(request):
    query=request.GET.get('query')

    blog=Post.objects.filter(title__icontains=query)
    page_number=request.GET.get('page')
    paginator=Paginator(blog,2)
    page_obj=paginator.get_page(page_number)
    return render(request,'home/home.html',{'blog':page_obj})
