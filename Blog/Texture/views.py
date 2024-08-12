from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import TextureForm
from .models import Textures, Category
from .utils import MyMixin


class HomeTexture(ListView, MyMixin):
    model = Textures
    context_object_name = 'textures'
    template_name = 'Texture/home_texture_list.html'
    extra_context = {'title': 'Главная'}
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Textures.objects.filter(is_published=True).select_related('category')


class TextureByCategory(ListView, MyMixin):
    model = Textures
    template_name = 'Texture/home_texture_list.html'
    context_object_name = 'textures'
    allow_empty = True
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return Textures.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class ViewTexture(DetailView):
    model = Textures
    template_name = 'Texture/view_texture.html'
    context_object_name = 'texture_item'


class AddTexture(CreateView):
    form_class = TextureForm
    template_name = 'Texture/add_texture.html'
    login_url = '/admin/'



