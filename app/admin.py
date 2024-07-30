from django.contrib import admin
from .models import CommissionCommu,User,CommissionCul,Coordination,Secteur,Section, CommissionDecen, CommissionFem, CommissionOrg, CommissionSocial, Membre,BureauNational,Commission
# Register your models here.

admin.site.register(Coordination)
admin.site.register(User)
admin.site.register(Membre)
admin.site.register(Secteur)
admin.site.register(Section)
admin.site.register(BureauNational)
admin.site.register(Commission)
admin.site.register(CommissionOrg)
admin.site.register(CommissionFem)
admin.site.register(CommissionCommu)
admin.site.register(CommissionCul)
admin.site.register(CommissionSocial)
admin.site.register(CommissionDecen)
