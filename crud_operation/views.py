from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import TemplateView
from rest_framework.views import APIView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework.response import Response
from .models import GrupoEconomico, Cedente, LimiteCreditoCedente
from .serializers import GrupoEconomicoSerializer, CedenteSerializer, LimiteCreditoCedenteSerializer
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import GrupoEconomicoForm, CedenteForm, LimiteCreditoCedenteForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class GrupoEconomicoView(TemplateView):
    template_name = 'crud/grupo_economico_list.html'


class GrupoEconomicoCreateView(SuccessMessageMixin, CreateView):
    model = GrupoEconomico
    form_class = GrupoEconomicoForm
    template_name = "crud/grupo_economico_add.html"
    success_url = reverse_lazy('grupo_economico')
    success_message = "Successfully created the record !"


class GrupoEconomicoUpdateView(SuccessMessageMixin, UpdateView):
    model = GrupoEconomico
    pk_url_kwarg = 'id_grupo_economico'
    form_class = GrupoEconomicoForm
    template_name = "crud/grupo_economico_add.html"
    success_url = reverse_lazy('grupo_economico')
    success_message = "Successfully updated the record !"


class GrupoEconomicoDeleteView(SuccessMessageMixin, DeleteView):
    model = GrupoEconomico
    pk_url_kwarg = 'id_grupo_economico'
    success_url = reverse_lazy('grupo_economico')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def post(self, *args, **kwargs):
        instance = self.get_object()
        try:
            instance.delete()
            messages.success(self.request, 'Successfully deleted the record !')
        except Exception as e:
            messages.warning(self.request, 'Record is not deleted due to Integrity Error')

        return redirect('grupo_economico')


class GrupoEconomicoDetailView(DetailView):
    model = GrupoEconomico
    pk_url_kwarg = 'id_grupo_economico'
    template_name = "crud/grupo_economico_detail.html"


class GrupoEconomicoAPIView(APIView):
    def get(self, request, format=None):
        page = int(request.GET.get('pagination[page]'))
        perpage = int(request.GET.get('pagination[perpage]'))

        grupoe_conomico = GrupoEconomico.objects.order_by('-data_atualizacao')
        count = grupoe_conomico.count()

        perpage = perpage if perpage else 30
        paginator = Paginator(grupoe_conomico, perpage)

        try:
            grupoe_conomico = paginator.page(page)
        except PageNotAnInteger:
            grupoe_conomico = paginator.page(1)
        except EmptyPage:
            grupoe_conomico = paginator.page(paginator.num_pages)

        result = GrupoEconomicoSerializer(grupoe_conomico, many=True).data

        meta = {
            "page": page,
            "pages": int(count/perpage),
            "perpage": perpage,
            "total": count,
        }

        data = {
            'meta' : meta,
            'data' : result
        }

        return Response(data)


class CedenteView(TemplateView):
    template_name = 'crud/cedente_list.html'


class CedenteCreateView(SuccessMessageMixin, CreateView):
    model = Cedente
    form_class = CedenteForm
    template_name = "crud/cedente_add.html"
    success_url = reverse_lazy('cedente')
    success_message = "Successfully created the record !"


class CedenteUpdateView(SuccessMessageMixin, UpdateView):
    model = Cedente
    pk_url_kwarg = 'id_cedente'
    form_class = CedenteForm
    template_name = "crud/cedente_add.html"
    success_url = reverse_lazy('cedente')
    success_message = "Successfully updated the record !"


class CedenteDeleteView(SuccessMessageMixin, DeleteView):
    model = Cedente
    pk_url_kwarg = 'id_cedente'
    success_url = reverse_lazy('cedente')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def post(self, *args, **kwargs):
        instance = self.get_object()
        try:
            instance.delete()
            messages.success(self.request, 'Successfully deleted the record !')
        except Exception as e:
            messages.warning(self.request, 'Record is not deleted due to Integrity Error')

        return redirect('cedente')


class CedenteDetailView(DetailView):
    model = Cedente
    pk_url_kwarg = 'id_cedente'
    template_name = "crud/cedente_detail.html"


class CedenteAPIView(APIView):
    def get(self, request, format=None):
        page = int(request.GET.get('pagination[page]'))
        perpage = int(request.GET.get('pagination[perpage]'))

        records = Cedente.objects.order_by('-data_atualizacao')
        count = records.count()

        perpage = perpage if perpage else 30
        paginator = Paginator(records, perpage)

        try:
            records = paginator.page(page)
        except PageNotAnInteger:
            records = paginator.page(1)
        except EmptyPage:
            records = paginator.page(paginator.num_pages)

        result = CedenteSerializer(records, many=True).data

        meta = {
            "page": page,
            "pages": int(count/perpage),
            "perpage": perpage,
            "total": count,
        }

        data = {
            'meta' : meta,
            'data' : result
        }

        return Response(data)


class LimiteCreditoCedenteView(TemplateView):
    template_name = 'crud/limite_credito_cedente_list.html'


class LimiteCreditoCedenteCreateView(SuccessMessageMixin, CreateView):
    model = LimiteCreditoCedente
    form_class = LimiteCreditoCedenteForm
    template_name = "crud/limite_credito_cedente_add.html"
    success_url = reverse_lazy('limite_credito_cedente')
    success_message = "Successfully created the record !"


class LimiteCreditoCedenteUpdateView(SuccessMessageMixin, UpdateView):
    model = LimiteCreditoCedente
    pk_url_kwarg = 'id_limite_credito_cedente'
    form_class = LimiteCreditoCedenteForm
    template_name = "crud/limite_credito_cedente_add.html"
    success_url = reverse_lazy('limite_credito_cedente')
    success_message = "Successfully updated the record !"


class LimiteCreditoCedenteDeleteView(SuccessMessageMixin, DeleteView):
    model = LimiteCreditoCedente
    pk_url_kwarg = 'id_limite_credito_cedente'
    success_url = reverse_lazy('limite_credito_cedente')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def post(self, *args, **kwargs):
        instance = self.get_object()
        try:
            instance.delete()
            messages.success(self.request, 'Successfully deleted the record !')
        except Exception as e:
            messages.warning(self.request, 'Record is not deleted due to Integrity Error')

        return redirect('limite_credito_cedente')


class LimiteCreditoCedenteDetailView(DetailView):
    model = LimiteCreditoCedente
    pk_url_kwarg = 'id_limite_credito_cedente'
    template_name = "crud/limite_credito_cedente_detail.html"


class LimiteCreditoCedenteAPIView(APIView):
    def get(self, request, format=None):
        page = int(request.GET.get('pagination[page]'))
        perpage = int(request.GET.get('pagination[perpage]'))

        records = LimiteCreditoCedente.objects.order_by('-data_atualizacao')
        count = records.count()

        perpage = perpage if perpage else 30
        paginator = Paginator(records, perpage)

        try:
            records = paginator.page(page)
        except PageNotAnInteger:
            records = paginator.page(1)
        except EmptyPage:
            records = paginator.page(paginator.num_pages)

        result = LimiteCreditoCedenteSerializer(records, many=True).data

        meta = {
            "page": page,
            "pages": int(count/perpage),
            "perpage": perpage,
            "total": count,
        }

        data = {
            'meta' : meta,
            'data' : result
        }

        return Response(data)
