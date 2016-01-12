from django.contrib import admin

# Register your models here.
from models import PrincipalInvestigator,YoungInvestigator

class PrincipalInvestigatorAdmin(admin.ModelAdmin):
    class Meta:
        model=PrincipalInvestigator
        
class YoungInvestigatorAdmin(admin.ModelAdmin):
    class Meta:
        model=YoungInvestigator
        
admin.site.register(PrincipalInvestigator, PrincipalInvestigatorAdmin)
admin.site.register(YoungInvestigator, YoungInvestigatorAdmin)
