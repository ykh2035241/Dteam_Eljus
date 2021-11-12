from django.shortcuts import render

from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "index.html"

class HomeView(LoginRequiredMixin,generic.TemplateView):
    template_name = "home.html"