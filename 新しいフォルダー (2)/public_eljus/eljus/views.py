from django.shortcuts import render

from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ProblemManage

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "index.html"

class HomeView(LoginRequiredMixin,generic.TemplateView):
    template_name = "home.html"

class EljusListView(LoginRequiredMixin, generic.ListView):
    model = ProblemManage
    template_name = 'eljus_list.html'
    paginate_by = 2

    def get_queryset(self):
        diaries = ProblemManage.objects.filter(user=self.request.user).order_by('-created_at')
        return diaries