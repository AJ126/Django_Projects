from django import forms
from testapp.models import *

class data_form(forms.ModelForm):
    class Meta:
        model=data
        fields=('name','contact','address','order')
        widgets={
        'name':forms.TextInput(attrs={'class':'form-control'}),
        'contact':forms.TextInput(attrs={'class':'form-control'}),
        'address':forms.Textarea(attrs={'class':'form-control'}),
        'order':forms.Textarea(attrs={'class':'form-control'}),
        }

class feedback_form(forms.ModelForm):
    class Meta:
        model=feedback
        fields=['name','feedback']
        widgets={
        'name':forms.TextInput(attrs={'class':'form-control'}),
        'feedback':forms.Textarea(attrs={'class':'form-control'})
        }
