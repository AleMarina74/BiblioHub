from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Prestamo

@login_required(login_url='login')
def prestamosviews(request):
    paginator = Paginator(Prestamo.objects.all(), 10)
    page_number = request.GET.get("page")
    context = {
        "page_heading": "Prestamos",
        "prestamos": paginator.get_page(page_number),
        "field_keys": [field.attname for field in Prestamo._meta.get_fields()],
        "USER": request.user
    }
    return render(request=request, template_name='prestamos.html', context=context)

class PrestamoCreate(LoginRequiredMixin,CreateView):
    model = Prestamo
    template_name = 'prestamo_form.html'
    fields = ['libro','cliente','fecha_prestamo','fecha_devolucion']
    success_url = reverse_lazy('prestamos')


class PrestamoDetail(LoginRequiredMixin,DetailView):
    model = Prestamo
    template_name = 'prestamo_detail.html'
    context_object_name = 'prestamo'


class PrestamoUpdate(LoginRequiredMixin,UpdateView):
    model = Prestamo
    template_name = 'prestamo_form.html'
    fields = ['libro','cliente', 'fecha_prestamo','fecha_devolucion']
    success_url = reverse_lazy('prestamos')


class PrestamoList(LoginRequiredMixin,ListView):
    model = Prestamo
    template_name = 'prestamo_list.html'
    context_object_name = 'prestamos'
