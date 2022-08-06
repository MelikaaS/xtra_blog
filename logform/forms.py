from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class SignupForm(UserCreationForm):
    first_name=forms.CharField()
    last_name=forms.CharField()
    email=forms.EmailField()
    # password1 = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model=User
        fields=('first_name','last_name','email','username','password1','password2')


########################
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')


#######################
class Login_form(forms.Form):
    username=forms.CharField(max_length=10,widget=forms.TextInput(attrs={'autofocus':True}))
    password=forms.CharField(label="password",widget=forms.PasswordInput(attrs={"autocomplete":"current-password"}))


    def clean(self):
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')

        if username is not None or password:
            self.user_cache=authenticate(username=username,password=password)
            if self.user_cache is None:
                raise ValidationError("check it",code="fail")

        return self.cleaned_data

    def get_user(self):
        return self.user_cache




