from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    categories=(
        ('travel','سفر'),
        ('events','رویدادها'),
        ('creative', 'خلاقیت'),
        ('design','طراحی'),
        ('business','تجارت'),
        ('music','موسیقی'),
        ('audio','شنیدنی'),
        ('artworks','هنر'),
        ('visual','دیداری')
    )
    title = models.CharField(max_length=50, blank=True, choices=categories)

    class Meta:
        verbose_name_plural='categories'


    def __str__(self):
        return self.title



class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,default=True, related_name='posts')
    category= models.ManyToManyField(Category,related_name='posts')
    title=models.CharField(max_length=30)#, verbose_name='pizza')
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='images/posts_image', default=True)
    slug=models.SlugField(null=True, unique=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:post_app',kwargs={'slug':self.slug})
    #
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug=slugify(self.title)
        super(Post, self).save()



class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField(default=True)
    date=models.DateTimeField(auto_now_add=True)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True,related_name='replies')
    # image=models.ImageField(upload_to='images/comments',default=True)

    class Meta:
        ordering=['date']

    def __str__(self):
        return self.text[:50]

