from django.shortcuts import render


def about(request):
    return render(request,'about/about.html')

# Create your views here.
