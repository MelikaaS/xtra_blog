from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from logform.forms import SignupForm, UserEditForm,Login_form

from myblog import settings

#####################
# def enter(request):
#     if request.method=='POST':
#         # form=Enterform(request.POST)
#         form=AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user=form.get_user()
#             login(request,user)
#             return redirect('home:home_app')
#
#     else:
#         # form=Enterform()
#         form=AuthenticationForm()
#     return render(request,'logform/login.html',{'form':form})

#####################
# def signin(request):
#     if request.user.is_authenticated:
#         return redirect('home:home_app')
#     if request.method == 'POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         user = authenticate(request,username=username,password=password)
#         if user is not None:
#             login(request,user)
#             subject='welcome'
#             email=settings.EMAIL_HOST_USER
#             message="welcome to xtra blog"
#             recepient_list=['ms_sos631@yahoo.com']
#             send_mail(subject,message,email,recepient_list)
#             return redirect('home:home_app')
#     return render(request,'logform/login.html')

def signout(request):
    logout(request)
    return redirect('home:home_app')


def signup(request):
    if request.method=="POST":
        # form=UserCreationForm(request.POST)
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            # username=form.cleaned_data.get('username')
            # password=form.cleaned_data.get('password1')
            # user=authenticate(username=username,password=password)
            # login(request,user)
            # print(username)
            return redirect('home:home_app')
    else:
        # form=UserCreationForm()
        form=SignupForm()
    return render(request,'logform/signup.html',{'form':form})



def edit_user(request):
    value=[1,2,3]
    user=request.user
    form = UserEditForm(instance=user)
    #now edit is statrting
    if request.method =="POST":
        form=UserEditForm(data=request.POST,instance=user)
        form.save()
        return redirect('home:home_app')
    return render(request,"logform/edit.html",{"form":form, 'value':value})

##############################
def login_view(request):
    if request.method=="POST":
        form=Login_form(request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect("home:home_app")
    else:
        form=Login_form()
    return render(request,'logform/login.html',{'form':form})



