from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import WorldForm
from .models import Worlds, Category
from .utils import MyMixin


class HomeWorld(ListView, MyMixin):
    model = Worlds
    context_object_name = 'worlds'
    template_name = 'World/home_world_list.html'
    extra_context = {'title': 'Главная'}
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Worlds.objects.filter(is_published=True).select_related('category')


class WorldByCategory(ListView, MyMixin):
    model = Worlds
    template_name = 'World/home_world_list.html'
    context_object_name = 'worlds'
    allow_empty = True
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return Worlds.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class ViewWorld(DetailView):
    model = Worlds
    template_name = 'World/view_world.html'
    context_object_name = 'world_item'


class AddWorld(CreateView):
    form_class = WorldForm
    template_name = 'World/add_world.html'
    login_url = '/admin/'

