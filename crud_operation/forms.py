from django import forms
from django.utils.translation import gettext, gettext_lazy as _, pgettext
from .models import GrupoEconomico, Cedente, LimiteCreditoCedente, Fundo


class GrupoEconomicoForm(forms.ModelForm):
    class Meta:
        model = GrupoEconomico
        exclude = ('id_grupo_economico', 'data_atualizacao', )


class CedenteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['grupo_economico_id_grupo_economico'] = forms.IntegerField()

    def clean(self):
        cleaned_data = super(CedenteForm, self).clean()
        id_grupo_economico = cleaned_data.get('grupo_economico_id_grupo_economico')
        if id_grupo_economico:
            try:
                grupo_economico = GrupoEconomico.objects.get(id_grupo_economico=id_grupo_economico)
            except Exception as e:
                grupo_economico = None
                self.add_error(
                    'grupo_economico_id_grupo_economico',
                     _("related id has not object found")
                )
            if grupo_economico:
                cleaned_data.update({'grupo_economico_id_grupo_economico': grupo_economico})
        return cleaned_data

    class Meta:
        model = Cedente
        exclude = ('id_cedente', 'data_atualizacao', )


class LimiteCreditoCedenteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fundo_id_fundo'] = forms.IntegerField()
        self.fields['cedente_id_cedente'] = forms.IntegerField()

    def clean(self):
        cleaned_data = super(LimiteCreditoCedenteForm, self).clean()
        fundo_id_fundo = cleaned_data.get('fundo_id_fundo')
        cedente_id_cedente = cleaned_data.get('cedente_id_cedente')

        if fundo_id_fundo:
            try:
                fundo = Fundo.objects.get(id_fundo=fundo_id_fundo)
            except Exception as e:
                fundo = None
                self.add_error(
                    'fundo_id_fundo',
                     _("related id has not object found")
                )
            if fundo:
                cleaned_data.update({'fundo_id_fundo': fundo})

        if cedente_id_cedente:

            try:
                cedente = Cedente.objects.get(id_cedente=cedente_id_cedente)
            except Exception as e:
                cedente = None
                self.add_error(
                    'cedente_id_cedente',
                     _("related id has not object found")
                )
            if cedente:
                cleaned_data.update({'cedente_id_cedente': cedente})

        return cleaned_data

    class Meta:
        model = LimiteCreditoCedente
        exclude = ('id_limite_credito_cedente', 'data_atualizacao', )
