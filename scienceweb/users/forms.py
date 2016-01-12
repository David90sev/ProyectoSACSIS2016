from django import forms
from models import PrincipalInvestigator,YoungInvestigator
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        #fields = ['username','password','first_name', 'last_name', 'email']
        fields = [ 'username','password','first_name', 'last_name', 'email']
        widgets = { 
            'username' : forms.TextInput(attrs={'required': True, 'size':30}),
            'password' : forms.PasswordInput(attrs={'required': True, 'size':30}),
            'first_name': forms.TextInput(attrs={'required': True, 'size': 30}), 
            'last_name': forms.TextInput(attrs={'required': True, 'size': 30}), 
            'email': forms.EmailInput(attrs={'required': True, 'size': 30}),
        }
        
class UserFormEdit(forms.ModelForm):
    
    class Meta:
        model = User
        #fields = ['username','password','first_name', 'last_name', 'email']
        fields = [ 'first_name', 'last_name', 'email']
        widgets = { 
            'first_name': forms.TextInput(attrs={'required': True, 'size': 30}), 
            'last_name': forms.TextInput(attrs={'required': True, 'size': 30}), 
            'email': forms.EmailInput(attrs={'required': True, 'size': 30}),
        }


class YoungInvestigatorForm(forms.ModelForm):

    class Meta:
        model = YoungInvestigator
        #fields = []
        exclude= ('user','photo')
        widgets = {
            'telephone': forms.TextInput(attrs={'required': True}),   
            'title' : forms.ChoiceField(attrs={'required': True}),
            'specialty' : forms.TextInput(attrs={'required': True}),
            'curriculum' : forms.FileField(),
            'photo' : forms.FileField(),
            'research_field' : forms.ChoiceField(attrs={'required': True}),
            'research_speciality' : forms.TextInput(attrs={'required': True}),
            'h_index' : forms.DecimalField(),
            'country' : forms.TextInput(attrs={'required': True}),
            'city' : forms.TextInput(attrs={'required': True}),
            'facebook_link' : forms.URLField(),
            'twitter_link' : forms.URLField(),
            'linkedIn_link' : forms.URLField(),
            'principal_text' : forms.Textarea(),
            'other_text' : forms.Textarea(),
        }
        
        
