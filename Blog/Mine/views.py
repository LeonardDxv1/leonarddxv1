from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponse
from .models import VisitorCount


def index(request):
    context = {
        'title': 'Imperator_XV'
    }
    return render(request, 'mine/index.html', context=context)


def visitor_count_view(request):
    total_visitors = VisitorCount.objects.count()
    unique_visitors = VisitorCount.objects.values('ip_address').distinct().count()

    context = {
        'total_visitors': total_visitors,
        'unique_visitors': unique_visitors,
    }
    return render(request, 'yourapp/visitor_count.html', context)
