from django.shortcuts import render

from contact.forms import ContactusForm
from contact.models import Message
from django.core.mail import send_mail

from myblog import settings


def contact(request):
    if request.method=='POST':
        form=ContactusForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            subject=form.cleaned_data['subject']
            text=form.cleaned_data['text']
            Message.objects.create(name=name,email=email,subject=subject,text=text)
            cc_myself=form.cleaned_data['cc_myself']

        # subjects="welcome to my site"
        # message="this is for test"
        # email_from=settings.EMAIL_HOST_USER
        # recepient_list=['ms_sos631@yahoo.com']
        # send_mail(subjects,message,email_from,recepient_list)
    else:
            form=ContactusForm()
    return render(request,'contact/contact.html',{'form':form})



# Create your views here.
