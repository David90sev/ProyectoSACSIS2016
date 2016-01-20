from django.shortcuts import render, render_to_response
from django.views.generic.base import TemplateView
from users.models import YoungInvestigator, PrincipalInvestigator,Keyword,\
    Investigation_Group, Invitation, Offer, Keyword
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from users.forms import YoungInvestigatorForm, PrincipalInvestigatorForm,\
    UserForm, InvestigationGroupForm, OfferForm
from django.template.loader import render_to_string
from django.core.mail.message import EmailMultiAlternatives, EmailMessage
from django.template.defaultfilters import striptags
from django.contrib.auth.models import User
import random
from django.http.response import HttpResponseRedirect
from django.db.models import Q
from datetime import datetime, timedelta

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
    
def view_profile_withId(request, userId):
    try:
        users = YoungInvestigator.objects.get(user_id__exact=userId)
        is_young=True
        is_principal=False
    except:
        users = PrincipalInvestigator.objects.get(user_id__exact=userId)
        is_young=False
        is_principal=True
    print request.user
    return render_to_response('users/profile_id.html',
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
    principal = PrincipalInvestigator.objects.filter(user_id=request.user.id)
    if len(principal)==1:
        man=principal[0]
        groups_list_as_manager = Investigation_Group.objects.filter(manager_id=man.id)
        invitations=Invitation.objects.filter(participant_id=man.id,is_accept=True)
        groups_list=[]
        if len(invitations)!=0:
            for invitation in invitations:
                groups_list += Investigation_Group.objects.filter(_id=invitation.group.id)
    
            
        has_groups = (len(groups_list)>0)
        has_manage_groups = (len(groups_list_as_manager)>0)
    
    return render_to_response('groups/list.html',
                              {'groups_list_as_manager':groups_list_as_manager,
                               'groups_list':groups_list,
                               'has_groups':has_groups,'has_manage_groups':has_manage_groups},
                              context_instance = RequestContext(request))
    
def group_create(request):
    if request.method=='POST':
        formulario = InvestigationGroupForm(request.POST,request.FILES)
        if formulario.is_valid():
              
                
            ##Creacion del grupo
            userId = request.user.id
            manager1 = PrincipalInvestigator.objects.filter(user_id=userId)[0]

            Investigation_Group.objects.create(
                              manager=manager1,
                              title=formulario.cleaned_data['title'],
                              description=formulario.cleaned_data['description'],
                              research_field=formulario.cleaned_data['research_field'],
                              research_speciality=formulario.cleaned_data['research_speciality'],
                              )                

            return HttpResponseRedirect('list')
            
    else:
        formulario = InvestigationGroupForm()
    
    return render_to_response('groups/create.html',
                              {'formulario':formulario},
                              context_instance = RequestContext(request))
    
def group_view(request, groupId):
    group=Investigation_Group.objects.filter(id=groupId)[0]
    manager1=PrincipalInvestigator.objects.filter(id=group.manager.id)[0]
    user_manager=User.objects.filter(id=manager1.user.id)[0]
    invitations=Invitation.objects.filter(group_id=group.id,is_accept=1)
    users=[]
    for inv in invitations:
        users+=User.objects.filter(id=inv.participant.id)
    
    
    return render_to_response('groups/view.html',
                              {'group':group,'manager':manager1,'user_manager':user_manager,'users':users},
                              context_instance = RequestContext(request))    



def add_participant(request, groupId, participantId):
    group=Investigation_Group.objects.filter(id=groupId)
    participant=PrincipalInvestigator.objects.filter(id=participantId)
    Invitation.objects.create(group=group,participant=participant)
    
    return render_to_response('groups/view.html',
                              {'group':group},
                              context_instance = RequestContext(request))  
    
    
def add_offer(request):
    principal = PrincipalInvestigator.objects.filter(user_id=request.user.id)
    if len(principal!=0):
        prin=principal[0]
    
    if request.method=='POST':
        formulario = OfferForm(request.POST)
        if formulario.is_valid():
              
            ##Creacion de la oferta
#                title=models.CharField(max_length=140)
#                 description=models.CharField(max_length=3000)
#                 deadline=models.DateField()
#                 publication_date=models.DateField()
#                 keywords=models.ManyToManyField(Keyword)
#                 principal=models.ForeignKey(PrincipalInvestigator, on_delete=models.CASCADE)

            offer_inst=Offer.objects.create(
                              principal=prin,
                              title=formulario.cleaned_data['title'],
                              description=formulario.cleaned_data['description'],
                              deadline=formulario.cleaned_data['deadline'],
                              publication_date=datetime.now(),
                              )
            
            #Keywords
            keywords=formulario.cleaned_data['keywords']
            if keywords!=None: 
            #la separamos por comas y eliminamos la ultima tupla si estaa vacia
                key_vector=keywords.split(",")
                if (key_vector[len(key_vector)-1].strip()==''):
                    key_vector.pop()
                
                if len(key_vector)!=0:
                    #linkeamos todas las keys con su oferta y le hacemos strip para quitarle espacios en blanco a izq y der
                    for keyword in keywords:
                        key = keyword.strip()
                        if key!='' or key!=None:
                            Keyword.objects.create(word=key.capitalize(),offer=offer_inst)
                    #capitalize() strip(' '), .split(", ")
            
            ###por aqui
            return HttpResponseRedirect('list')
            
    else:
        formulario = OfferForm()
    
    return render_to_response('offer/create.html',
                              {'formulario':formulario},
                              context_instance = RequestContext(request))
        
    
    
def remove_offer(request,offerId):
    principal = PrincipalInvestigator.objects.filter(user_id=request.user.id)
    if len(principal!=0):
        prin=principal[0]
        Offer.objects.filter(id=offerId,principal=prin).delete()
    
    return HttpResponseRedirect('list')

def list_my_offers(request):
    principal = PrincipalInvestigator.objects.filter(user_id=request.user.id)
    offers=[]
    if len(principal!=0):
        prin=principal[0]
        offers=Offer.objects.filter(principal=prin)
        
    return render_to_response('offer/list.html',
                              {'offers':offers},
                              context_instance = RequestContext(request))

def list_offers_by_keywords(request):    
    young_v = YoungInvestigator.objects.filter(user_id=request.user.id)
    offers=[]
    if len(young_v)!=0:
        young=young_v[0]
        keys_young=Keyword.objects.filter(young=young)
        s=""
        for key in keys_young:
            s+=" OR `users_keyword`.word='"+key.word+"'"
        s=s[3:]
        query="SELECT DISTINCT `users_offer`.`id`, `users_offer`.`title`,`users_offer`.`description`,"
        query+=" `users_offer`.`deadline`, `users_offer`.`publication_date`, `users_offer`.`principal_id` FROM"
        query+=" `users_keyword_offer` , `users_keyword`, `users_offer` WHERE  `users_keyword`.id=`users_keyword_offer`.keyword_id "
        query+="AND `users_keyword_offer`.offer_id=`users_offer`.id AND ("+s+")"

        offers=Offer.objects.raw(query)
#       Offer.objects.raw('SELECT * FROM myapp_person WHERE last_name = %s', [lname])

# para una sola keyword Offer.objects.filter(Q(keywords__word=key.word))
        return render_to_response('offer/list.html',
                                    {'offers':offers},
                                    context_instance = RequestContext(request))    
    return HttpResponseRedirect('')


def list_offers_by_one_keyword(request, keyword):    
    key=Keyword.objects.filter(word=keyword)[0]
    offers=Offer.objects.filter(Q(keywords__word=key.word))
    return render_to_response('offer/list.html',
                                    {'offers':offers,'keyword':keyword},
                                    context_instance = RequestContext(request))    

    
##Para ordenar por h_index listas 
def compara( x, y ) :

    # x e y son objetos de los que se desea ordenar
    
    if x.h_index < y.h_index :
        rst = 1
    elif x.h_index > y.h_index :
        rst = -1
    else :
        rst = 0

    return rst

def search_user(request):
    query = request.GET.get('q', '')
    a=datetime.now() - timedelta(seconds=(365.25*24*60*60))
    if query:
        qset = (
            Q(username__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)|
            Q(last_login__gt=a)
        )
        results = User.objects.filter(qset).distinct()
        investigadores=[]
        for r in results:
            try:
                investigadores += YoungInvestigator.objects.filter(user_id=r.id)
            except:
                None
            try:
                investigadores += PrincipalInvestigator.objects.filter(user_id=r.id)
            except:
                None
        investigadores.sort(compara)
    else:
        results = User.objects.filter(is_staff=0)
        investigadores=[]
        for r in results:
            try:
                investigadores += YoungInvestigator.objects.filter(user_id=r.id)
            except:
                None
            try:
                investigadores += PrincipalInvestigator.objects.filter(user_id=r.id)
            except:
                None
        investigadores.sort(compara)
    return render_to_response("users/list.html", {
        "results": investigadores,
        "query": query
    },context_instance = RequestContext(request))