from django import forms
from django.core.exceptions import ValidationError
from setuptools._entry_points import _

from contact.models import Message


# class ContactusForm(forms.Form):
#     year=range(1300,1401,1)
#     # month=['فروردین','اردیبهشت','خرداد','تیر','مرداد','شهریور','مهر','آبان','آذر','دی','بهمن','اسفند']
#     month={
#         1:"فروردین", 2:"اردیبهشت" , 3:"خرداد", 4:"تیر", 5:"مرداد", 6:"شهریور", 7:"مهر", 8:"آبان", 9:"آذر", 10:"دی", 11:"بهمن", 12:"اسفند"
#     }
#     # month = {
#     #     1: _('jan'), 2: _('feb'), 3: _('mar'), 4: _('apr'),
#     #     5: _('may'), 6: _('jun'), 7: _('jul'), 8: _('aug'),
#     #     9: _('sep'), 10: _('oct'), 11: _('nov'), 12: _('dec')
#     # }
#     favorite_color=[('blue','Blue'),
#                     ('green','Green'),
#                     ('yellow','Yellow')
#                     ]
#
#     birth_year=forms.DateField(widget=forms.SelectDateWidget(years=year,months=month))
#     # fav_color=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=favorite_color)
#     fav_color=forms.ChoiceField(widget=forms.RadioSelect,choices=favorite_color)
#     name=forms.CharField(max_length=5)
#     email=forms.CharField(max_length=30)
#     subject=forms.CharField(max_length=20)
#     text=forms.CharField(max_length=200)
#     cc_myself=forms.BooleanField(required=True)

class ContactusForm(forms.ModelForm):
    birth_year = forms.DateField(widget=forms.SelectDateWidget())
    class Meta:
        model=Message
        fields='__all__'
        widgets = {
            "email": forms.EmailInput(attrs={'class':'form-control',
                                             'placeholder':'write your email'}),
            "name":forms.TextInput(attrs={'disabled':True})
        }

    def clean(self):
        name=self.cleaned_data.get('name')
        text=self.cleaned_data.get('text')
        email=self.cleaned_data.get('email')
        if '@' not in email:
            self.add_error('email','correct email')
        if name==text:
            raise ValidationError('error: name and text are the same,please correct the error',code='name_text_same')




    # def clean_email(self):
    #     email=self.cleaned_data.get('email')
    #     if '@' not in email:
    #         raise ValidationError('error:please write the correct email', code='fault_email')
    #     return email
