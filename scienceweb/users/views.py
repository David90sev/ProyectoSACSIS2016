from django.shortcuts import render, render_to_response
from django.views.generic.base import TemplateView
from users.models import YoungInvestigator, PrincipalInvestigator,\
    Investigation_Group
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from users.forms import YoungInvestigatorForm, PrincipalInvestigatorForm,\
    UserForm
from django.template.loader import render_to_string
from django.core.mail.message import EmailMultiAlternatives, EmailMessage
from django.template.defaultfilters import striptags
from django.contrib.auth.models import User
import random

# Create your views here.
@login_required
def view_profile(request):
    try:
        users = YoungInvestigator.objects.get(user_id__exact=request.user.id)
        is_young=True
        is_principal=False
    except:
        users = PrincipalInvestigator.objects.get(user_id__exact=request.user.id)
        is_young=False
        is_principal=True
    print request.user
    return render_to_response('users/profile.html',
                              {'users':users,'is_young':is_young,'is_principal':is_principal},
                              context_instance = RequestContext(request))


def registration_young_inv(request):
    if request.method=='POST':
        userForm = UserForm(request.POST)
        formulario = YoungInvestigatorForm(request.POST)
        if userForm.is_valid():
            if (formulario.is_valid() and userForm.is_valid()):
                first_name=userForm.cleaned_data['first_name']
                last_name=userForm.cleaned_data['last_name']
                username=userForm.cleaned_data['username']
                email=userForm.cleaned_data['email']
                telephone=formulario.cleaned_data['telephone']
#                 title = formulario.cleaned_data['title']
#                 specialty = formulario.cleaned_data['specialty']
#                 research_field=formulario.cleaned_data['research_field']
#                 research_speciality=formulario.cleaned_data['research_speciality']
#                 h_index=formulario.cleaned_data['h_index']
#                 country=formulario.cleaned_data['country']
#                 city=formulario.cleaned_data['city']
#                 facebook_link=formulario.cleaned_data['facebook_link']
#                 twitter_link=formulario.cleaned_data['twitter_link']
#                 linkedIn_link=formulario.cleaned_data['linkedIn_link']
#                 principal_text=formulario.cleaned_data['principal_text']
#                 other_text=formulario.cleaned_data['specialty']
#               autogenerado   token=

                
                
                ##Creacion de usuario
                user1 = User(username=userForm.cleaned_data['username'],
                                           first_name=userForm.cleaned_data['first_name'],
                                           last_name=userForm.cleaned_data['last_name'],
                                           email=userForm.cleaned_data['email'],
                                           is_active=0,)
                #Le asignamos la clave encriptada
                user1.set_password(userForm.cleaned_data['password'])
                user1.save()
                
                ##Activation Link
                           
                activation_key = ''.join(random.choice('123456789abcdefghijklmnopqrstuvwxyz') for _ in range(20))
                
                ctx_dict = {'activation_key': activation_key,
                            'first_name': first_name,
                            'last_name': last_name,
                            'username': username,
                            'email': email,
                            'telephone': telephone,}
    
                
                ##Editor
                young=YoungInvestigator.objects.create( user = user1,
                                                        telephone =formulario.cleaned_data['telephone'] ,
                                                        title = formulario.cleaned_data['title'],
                                                        specialty = formulario.cleaned_data['specialty'],
                                                        research_field=formulario.cleaned_data['research_field'],
                                                        research_speciality=formulario.cleaned_data['research_speciality'],
                                                        h_index=formulario.cleaned_data['h_index'],
                                                        country=formulario.cleaned_data['country'],
                                                        city=formulario.cleaned_data['city'],
                                                        facebook_link=formulario.cleaned_data['facebook_link'],
                                                        twitter_link=formulario.cleaned_data['twitter_link'],
                                                        linkedIn_link=formulario.cleaned_data['linkedIn_link'],
                                                        principal_text=formulario.cleaned_data['principal_text'],
                                                        other_text=formulario.cleaned_data['other_text'],
                                                        token=activation_key,)


                
                
                ##envio correo al editor
                mail_text = striptags('')
                from_email= 'dalcantara@peerland.org'
                html_content = render_to_string('users/activation_email_for_user.txt',ctx_dict)
                msg1 = EmailMultiAlternatives("User registration request for ScienceWeb", mail_text, from_email, [email])
                msg1.attach_alternative(html_content, "text/html")
                msg1.send()
                
                return render_to_response('users/registration_complete.html')
            
    else:
        formulario = YoungInvestigatorForm()
        userForm = UserForm()
    
    return render_to_response('users/registration_form.html',
                              {'formulario':formulario,'userForm':userForm,'urlRequest':"/users/register_yi"},
                              context_instance = RequestContext(request))
    
def registration_principal_inv(request):
    if request.method=='POST':
        formulario = PrincipalInvestigatorForm(request.POST)
        userForm = UserForm(request.POST)
        if userForm.is_valid():
            if (formulario.is_valid() and userForm.is_valid()):
                first_name=userForm.cleaned_data['first_name']
                last_name=userForm.cleaned_data['last_name']
                username=userForm.cleaned_data['username']
                email=userForm.cleaned_data['email']
                telephone=formulario.cleaned_data['telephone']
#                 research_field=formulario.cleaned_data['research_field']
#                 research_speciality=formulario.cleaned_data['research_speciality']
#                 h_index=formulario.cleaned_data['h_index']
#                 country=formulario.cleaned_data['country']
#                 city=formulario.cleaned_data['city']
#                 facebook_link=formulario.cleaned_data['facebook_link']
#                 twitter_link=formulario.cleaned_data['twitter_link']
#                 linkedIn_link=formulario.cleaned_data['linkedIn_link']
#                 principal_text=formulario.cleaned_data['principal_text']
#                 other_text=formulario.cleaned_data['specialty']
#                 number_of_authorisating=formulario.cleaned_data['number_of_authorisating']
#                 offers_text=formulario.cleaned_data['offers_text']
#                 interested_in_premium=formulario.cleaned_data['interested_in_premium']
                # autogenerado   token=


                
                
                ##Creacion de usuario
                user1 = User(username=userForm.cleaned_data['username'],
                                           first_name=userForm.cleaned_data['first_name'],
                                           last_name=userForm.cleaned_data['last_name'],
                                           email=userForm.cleaned_data['email'],
                                           is_active=0,)
                #Le asignamos la clave encriptada
                user1.set_password(userForm.cleaned_data['password'])
                user1.save()
                
                ##Activation Link
                           
                activation_key = ''.join(random.choice('123456789abcdefghijklmnopqrstuvwxyz') for _ in range(20))
                
                ctx_dict = {'activation_key':activation_key,
                            'first_name': first_name,
                            'last_name': last_name,
                            'username': username,
                            'email': email,
                            'telephone': telephone,
                            }
    
                
                ##Editor
                principal=PrincipalInvestigator.objects.create( user = user1,
                                                        telephone =formulario.cleaned_data['telephone'] ,
                                                        research_field=formulario.cleaned_data['research_field'],
                                                        research_speciality=formulario.cleaned_data['research_speciality'],
                                                        h_index=formulario.cleaned_data['h_index'],
                                                        country=formulario.cleaned_data['country'],
                                                        city=formulario.cleaned_data['city'],
                                                        facebook_link=formulario.cleaned_data['facebook_link'],
                                                        twitter_link=formulario.cleaned_data['twitter_link'],
                                                        linkedIn_link=formulario.cleaned_data['linkedIn_link'],
                                                        principal_text=formulario.cleaned_data['principal_text'],
                                                        other_text=formulario.cleaned_data['other_text'],
                                                        number_of_authorisating=formulario.cleaned_data['number_of_authorisating'],
                                                        offers_text=formulario.cleaned_data['offers_text'],
                                                        interested_in_premium=formulario.cleaned_data['interested_in_premium'],
                                                        token=activation_key,)


                
                
                ##envio correo al editor
                mail_text = striptags('')
                from_email= 'dalcantara@peerland.org'
                html_content = render_to_string('users/activation_email_for_user.txt',ctx_dict)
                msg1 = EmailMultiAlternatives("User registration request for ScienceWeb", mail_text, from_email, [email])
                msg1.attach_alternative(html_content, "text/html")
                msg1.send()
                
                return render_to_response('users/registration_complete.html')
        
    else:
        formulario = PrincipalInvestigatorForm()
        userForm = UserForm()
    
    return render_to_response('users/registration_form.html',
                              {'formulario':formulario,'userForm':userForm, 'urlRequest':"/users/register_pi"},
                              context_instance = RequestContext(request))

def registration_choose(request):
    return render_to_response('users/registration_choose.html',context_instance = RequestContext(request))

def activate(request, token):

    
    aux1=YoungInvestigator.objects.filter(token=token)
    aux2=PrincipalInvestigator.objects.filter(token=token)
    aux=[]
    if len(aux1)==1:
        aux=aux1
    if len(aux2)==1:
        aux=aux2
    if len(aux)==1:
        reg1=aux[0]
        user1=User.objects.filter(id=reg1.user.id)[0]
        user1.is_active=1
        user1.save()
        reg1.activation_key="ALREADY_ACTIVATED"
        reg1.save()
        
        ##correo para informar de la activacion
        contenido="Thanks for trust in ScienceWeb.\n You can access with your account.\n\nUsername: "+user1.username+"\n http://www.peerland.org/"
        correo = EmailMessage("ScienceWeb: Your Account is already activated", contenido, to=[user1.email])
        correo.send()
        
        return render_to_response('users/activation_complete.html',context_instance = RequestContext(request))
    
    else:
        return render_to_response('users/activate.html')
    
@login_required
def list_investigation_groups(request):
    userId = request.user.id
    manager = PrincipalInvestigator.objects.filter(user_id=userId)
    groups_list = Investigation_Group.objects.filter(manager_id=manager.id)
    has_groups = (len(groups_list)>0)
    
    return render_to_response('groups/listMYgroupss.html',
                              {'groups_list':groups_list,'has_groups':has_groups},
                              context_instance = RequestContext(request))
