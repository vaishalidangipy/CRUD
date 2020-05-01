from django.contrib import admin
from .models import GrupoEconomico, Cedente, LimiteCreditoCedente


class CedenteAdmin(admin.ModelAdmin):
    readonly_fields = ['grupo_economico_id_grupo_economico', 'cadastro_grupo']


admin.site.register(GrupoEconomico)
admin.site.register(Cedente, CedenteAdmin)
admin.site.register(LimiteCreditoCedente)


