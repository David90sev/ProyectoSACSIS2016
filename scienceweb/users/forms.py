from django import forms
from django.contrib.auth.models import User
from models import *

TITLES_AVALIAVLE=(("Graduate","Graduate"),
                  ("Doctor","Doctor"),)

RESEARCH_FIELD_CHOOSES=(("All","All"),
                          ("Agricultural sciences","Agricultural sciences"),
                          ("Anthropology","Anthropology"),
                          ("Architecture","Architecture"),
                          ("Arts","Arts"),
                          ("Astronomy","Astronomy"),
                          ("Biological sciences","Biological sciences"),
                          ("Chemistry","Chemistry"),
                          ("Communication sciences","Communication sciences"),
                          ("Computer science","Computer science"),
                          ("Criminology","Criminology"),
                          ("Cultural studies","Cultural studies"),
                          ("Demography","Demography"),
                          ("Economics","Economics"),
                          ("Educational sciences","Educational sciences"),
                          ("Engineering","Engineering"),
                          ("Environmental science","Environmental science"),
                          ("Ethics in health sciences","Ethics in health sciences"),
                          ("Ethics in natural sciences","Ethics in natural sciences"),
                          ("Ethics in physical sciences","Ethics in physical sciences"),
                          ("Ethics in social sciences","Ethics in social sciences"),
                          ("Geography","Geography"),
                          ("Geosciences","Geosciences"),
                          ("History","History"),
                          ("Information science","Information science"),
                          ("Juridical sciences","Juridical sciences"),
                          ("Language sciences","Language sciences"),
                          ("Literature","Literature"),
                          ("Mathematics","Mathematics"),
                          ("Mecical sciences","Mecical sciences"),
                          ("Neurosciences","Neurosciences"),
                          ("Other","Other"),
                          ("Pharmacological sciences","Pharmacological sciences"),
                          ("Philosophy","Philosophy"),
                          ("Physics","Physics"),
                          ("Political sciences","Political sciences"),
                          ("Psychological sciences","Psychological sciences"),
                          ("Religious Sciences","Religious Sciences"),
                          ("Sociology","Sociology"),
                          ("Technology","Technology"),)

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
        exclude= ('user','photo','curriculum','token')
        widgets = {

        }
        telephone = forms.TextInput(attrs={'required': True}),   
        title = forms.ChoiceField(widget=forms.Select(),choices=TITLES_AVALIAVLE),
        specialty = forms.TextInput(attrs={'required': True}),
        research_field = forms.ChoiceField(widget=forms.Select(),choices=RESEARCH_FIELD_CHOOSES,),
        research_speciality = forms.TextInput(attrs={'required': True}),
        h_index = forms.IntegerField(),
        country = forms.TextInput(attrs={'required': True}),
        city = forms.TextInput(attrs={'required': True}),
        facebook_link = forms.URLField(),
        twitter_link = forms.URLField(),
        linkedIn_link = forms.URLField(),
        principal_text = forms.Textarea(),
        other_text = forms.Textarea(),
        fields=['telephone','title','specialty','research_field','research_speciality','h_index','country','city',
                'facebook_link','twitter_link','linkedIn_link','principal_text','other_text',]
        

class PrincipalInvestigatorForm(forms.ModelForm):

    class Meta:
        model = PrincipalInvestigator
        #fields = []
        exclude= ('user','photo','curriculum','token')
        widgets = {
#             'curriculum' : forms.FileField(),
#             'photo' : forms.FileField(),
#             'research_field' : forms.ChoiceField(widget=forms.Select(),choices=RESEARCH_FIELD_CHOOSES),
        }
        telephone = forms.TextInput(attrs={'required': True}),   
        research_field = forms.ChoiceField(widget=forms.Select())
        research_speciality = forms.TextInput(attrs={'required': True}),
        h_index = forms.IntegerField(),
        country = forms.TextInput(attrs={'required': True}),
        city = forms.TextInput(attrs={'required': True}),
        facebook_link = forms.URLField(),
        twitter_link = forms.URLField(),
        linkedIn_link = forms.URLField(),
        principal_text = forms.Textarea(),
        other_text = forms.Textarea(),
        number_of_authorisating = forms.IntegerField(),
        interested_in_premium = forms.BooleanField(),
        fields = ['telephone','research_field','research_speciality','h_index','country','city','facebook_link',
                  'twitter_link','linkedIn_link','principal_text','other_text','number_of_authorisating'
                  ,'interested_in_premium']

class InvestigationGroupForm(forms.ModelForm):
    class Meta:
        model = Investigation_Group
        #fields = []
        exclude= ('manager',)
        widgets = {}
        title=forms.TextInput(attrs={'required': True})
        description=forms.Textarea(attrs={'required': True})
        research_field = forms.ChoiceField(widget=forms.Select())
        research_speciality = forms.TextInput(attrs={'required': True}),                                        
        fields =['title','description','research_field','research_speciality']
        
class OfferForm(forms.ModelForm):
    
    class Meta:
        model = Offer
        #fields = []
        exclude= ('principal','publication_date',)
        widgets = {}
        title=forms.TextInput(attrs={'required': True})
        description=forms.Textarea(attrs={'required': True})
        deadline=forms.DateField()
#         keywords = forms.TextInput(attrs={'required': True})
        fields =['title','description','deadline']

class KeywordsForm(forms.ModelForm):
    
    class Meta:
        model=Keyword
        exclude=('young','principal','offer')
        widgets = {'word':forms.TextInput(attrs={'required': True}),}
