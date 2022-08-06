from django.shortcuts import render

from post.models import Post, Comment


def post(request,slug):#title):#id):
    blog=Post.objects.get(slug=slug)#title=title)#id=id)
    # comment=Comment.objects.all()
    if request.method=='POST':
        text=request.POST.get('text')
        parent_id=request.POST.get('parent_id')
        Comment.objects.create(user=request.user, text=text, post=blog,parent_id=parent_id)

    return render(request,'post/post.html',{'item':blog})#,'comment':comment})

# def sidebar(request):
#     return render(request,'includes/sidebar.html',context={'name':"LOVE"})
#


# Create your views here.
