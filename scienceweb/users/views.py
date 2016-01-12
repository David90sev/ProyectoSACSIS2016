from django.shortcuts import render
from django.views.generic.base import TemplateView
from users.models import YoungInvestigator, PrincipalInvestigator

# Create your views here.
class home(TemplateView):        

    try:
        context['user'] = EditorProfile.objects.get(user_id__exact=self.request.user.id)
    except:
        context['user'] = None
        
    ##TAMBIEN ES REVIEWER
    try:
        context['is_young'] = YoungInvestigator.objects.get(user_id__exact=self.request.user.id)!=None
    except:
        context['is_young'] = None
        
    #ES OWNER DE ALGUN JOURNAL
    try:
        context['is_principal'] = PrincipalInvestigator.objects.get(user_id__exact=self.request.user.id)!=None
    except:
        context['is_owner'] = None
        
#         try:
#             context['inbox'] = inbox_count_for(self.request.user)
#         except:
#             context['inbox'] = None




        return context

        return super(HomePageView, self).dispatch(*args, **kwargs)
    
    