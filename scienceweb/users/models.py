from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator
from django.db.models.fields import CharField

# Create your models here.
class YoungInvestigator(models.Model):

    user = models.OneToOneField(User, unique=True, related_name='young_investigator')
    telephone = models.CharField(max_length=13,validators=[RegexValidator(regex='^\d{9}$', message='Must need to be a real number', code='nomatch')])
    #Fields for title
    TITLES_AVALIAVLE=(("Graduate","Graduate"),
                      ("Doctor","Doctor"),)
    title = models.CharField(max_length=30,choices=TITLES_AVALIAVLE,default="Graduate")
    specialty = models.CharField(max_length=100)
    curriculum = models.FileField(upload_to = 'user/curriculum')
    photo = models.ImageField(upload_to='users/photos', default='users/photos/nouser.png', help_text="Maximun photo size = 256 Kb")
    #Fields for research fields
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
    research_field=models.CharField(max_length=30,choices=RESEARCH_FIELD_CHOOSES,default="All")
    research_speciality=models.CharField(max_length=100)
    h_index=models.DecimalField(max_digits=5, decimal_places=2)
    country=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    facebook_link=models.URLField()
    twitter_link=models.URLField()
    linkedIn_link=models.URLField()
    principal_text=models.CharField(max_length=500)
    other_text=models.CharField(max_length=500)
    
    
    class Meta:
        verbose_name = 'young_investigator'
        verbose_name_plural = 'young_investigators'
    
    def __unicode__(self):
        return u"Young_investigator information for %s" % self.user.username
    
    
class PrincipalInvestigator(models.Model):

    user = models.OneToOneField(User, unique=True, related_name='principal_investigator')
    telephone = models.CharField(max_length=13,validators=[RegexValidator(regex='^\d{9}$', message='Must need to be a real number', code='nomatch')])
    curriculum = models.FileField(upload_to = 'user/curriculum')
    photo = models.ImageField(upload_to='users/photos', default='users/photos/nouser.png', help_text="Maximun photo size = 256 Kb")
    #Fields for research fields
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
    research_field=models.CharField(max_length=2,choices=RESEARCH_FIELD_CHOOSES,default="All")
    research_speciality=models.CharField(max_length=100)
    h_index=models.DecimalField(max_digits=5, decimal_places=2)
    country=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    facebook_link=models.URLField()
    twitter_link=models.URLField()
    linkedIn_link=models.URLField()
    number_of_authorisating=models.IntegerField()
    principal_text=models.CharField(max_length=500)
    offers_text=models.CharField(max_length=1500)
    other_text=models.CharField(max_length=500)
    interested_in_premium=models.BooleanField()
    
    
    class Meta:
        verbose_name = 'principal_investigator'
        verbose_name_plural = 'principal_investigators'
    
    def __unicode__(self):
        return u"Principal_investigator information for %s" % self.user.username
