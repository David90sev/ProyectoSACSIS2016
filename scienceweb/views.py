
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, FormView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.core.mail import EmailMessage
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

#from registration.models import RegistrationProfile
#from django.shortcuts import render_to_response
#from forms import ContactForm
#from django.core.context_processors import csrf
#from django.http import HttpResponseRedirect

########################################
#### SEND NEW PASSWORD - FORGOT PASS ###
########################################
class SendPasswordView (FormView):
    template_name = "registration/sendPassword.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy('accounts_login')
    error_url = reverse_lazy('accounts_login')


    def success_url_calculate(self, user):
        self.success_url = reverse_lazy('accounts_login')


    def form_valid(self, form):
        
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
               
        user = authenticate(username=username, email=email)
        
        if user is not None:       
            if user.is_active:
                
                login(self.request, user)
                self.success_url_calculate(user)

            else:
                self.success_url = reverse_lazy('accounts_login')
        else:
            self.success_url = reverse_lazy('accounts_login')

        return redirect(self.success_url)


    def form_invalid(self):
        return redirect(self.error_url)


    def post(self, request, *args, **kwargs):
        username1 = request.POST['username']
        email1 = request.POST['email']
        
        #Generamos la password
        aux=User.objects.filter(email__contains= email1 ).filter(username= username1)
        passwordP= User.objects.make_random_password(length=10, allowed_chars='123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
        
        #Recorremos si existe, y debe ser unico, los resultados obtenidos de la busqueda, cambiando y mandando el correo
        for res in aux:
            res.set_password(passwordP)
            res.save()
                 
            titulo = 'Your new Password '+res.username+'from Peerland'
            contenido='Your password change request has been accepted, these are the details of your new user access.'
            contenido+= '\n\nUsername: '+ res.username
            contenido+= '\nPassword: '+ passwordP
            contenido+= '\n\nIf you have not requested any password change, please, contact us. Thanks '

            
            #correo para enviar
            correo = EmailMessage(titulo, contenido, to=[res.email])
            correo.send()
                   
        return redirect(self.success_url)



    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            self.success_url_calculate(self.request.user)
            return redirect(self.success_url)

        return super(SendPasswordView, self).dispatch(*args, **kwargs)



########################################
####             Logout              ###
########################################    
#def logout_view(request):
 #   logout(request)
  #  return render_to_response("home.html")

 
 
 
########################################
####        Static templates         ###
########################################
#def static(request,option):
 #   return render_to_response("static/"+option,{},context_instance = RequestContext(request))



########################################
####           HomeView              ###
########################################
class HomeView (TemplateView):
    template_name = "home.html"



########################################
####           LoginView             ###
########################################   
# class LoginView (FormView):
#     template_name = "registration/login.html"
#     form_class = AuthenticationForm
#     success_url = reverse_lazy('home_site')
#     error_url = reverse_lazy('accounts_login')
# 
# 
#     def success_url_calculate(self, user):
#         try:
#             reg = RegistrationProfile.objects.get(user_id__exact=user.pk)        
#             if reg != None:
#                 if reg.is_reviewer == 1:
#                     self.success_url = reverse_lazy('reviewer_home')
#                 if reg.is_editor == 1:
#                     self.success_url = reverse_lazy('editor_home')
#                 if reg.is_organization == 1:
#                     self.success_url = reverse_lazy('organization_home')
#         except:
#             self.success_url = reverse_lazy('home_site')
# 
# 
#     def form_valid(self, form):
#         
#         username = form.cleaned_data['username']
#         password = form.cleaned_data['password']
#                
#         user = authenticate(username=username, password=password)
#         
#         if user is not None:       
#             if user.is_active:
#                 
#                 login(self.request, user)
#                 self.success_url_calculate(user)
# 
#             else:
#                 self.success_url = reverse_lazy('accounts_login')
#         else:
#             self.success_url = reverse_lazy('accounts_login')
# 
#         return redirect(self.success_url)
# 
# 
#     def form_invalid(self):
#         return redirect(self.error_url)
# 
# 
#     def post(self, request, *args, **kwargs):
#         if "signup" in request.POST:
#             return redirect('/accounts/register/')
# 
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         if form.is_valid():
#             return self.form_valid(form)
#         else:               
#             return self.form_invalid()
# 
# 
#     def dispatch(self, *args, **kwargs):
#         if self.request.user.is_authenticated():
#             self.success_url_calculate(self.request.user)
#             return redirect(self.success_url)
# 
#         return super(LoginView, self).dispatch(*args, **kwargs)
# 
# 
# ########################################
# ####           Feedback              ###
# ########################################    
# def feedback(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             topic = form.cleaned_data['topic']
#             message = form.cleaned_data['message']
#             
#             correo = EmailMessage('Feedback from Peerland.org, topic: %s' % topic,
#                                    message,
#                                     to=['dalcantara@peerland.org']
#                                   )
# 
#             correo.send()
#             return render_to_response('feedback/thanks.html')
# 
#     else:
#         form = ContactForm()
#         
#     args = {'form':form}
#     args.update(csrf(request))
#     return render_to_response('feedback/feedback.html', args)