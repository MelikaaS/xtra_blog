from post.models import Post,Category


def global_data(request):
    category=Category.objects.all()[0:3]
    post=Post.objects.all()[0:4]

    return {'category':category, 'post':post}

    # return {'blog': blog}