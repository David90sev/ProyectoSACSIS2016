from django.contrib import admin

# Register your models here.
from models import PrincipalInvestigator,YoungInvestigator
from users.models import Keyword, Offer

class PrincipalInvestigatorAdmin(admin.ModelAdmin):
    class Meta:
        model=PrincipalInvestigator
        
class YoungInvestigatorAdmin(admin.ModelAdmin):
    class Meta:
        model=YoungInvestigator

class OfferAdmin(admin.ModelAdmin):
    class Meta:
        model=Offer

class KeywordAdmin(admin.ModelAdmin):
    class Meta:
        model=Keyword
        
        
        
        
admin.site.register(PrincipalInvestigator, PrincipalInvestigatorAdmin)
admin.site.register(YoungInvestigator, YoungInvestigatorAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Keyword, KeywordAdmin)

