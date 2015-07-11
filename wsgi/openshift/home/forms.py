from django import forms
from .models import User,Message
from django.core.exceptions import ObjectDoesNotExist

class ContactForm(forms.Form):
	name=forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name','required':True}))
	email=forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email','required':True,'type':'email'}))
	message=forms.CharField(label='',widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Message','required':True}))
