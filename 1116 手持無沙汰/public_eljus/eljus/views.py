from django.shortcuts import render

from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# from .forms import ProblemCreateForm #p271 1116
from .models import ProblemManage

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "index.html"

class HomeView(LoginRequiredMixin,generic.TemplateView):
    template_name = "home.html"

class ProblemListView(LoginRequiredMixin, generic.ListView):
    model = ProblemManage
    template_name = 'problem_list.html'
    paginate_by = 2

    def get_queryset(self):
        eljus = ProblemManage.objects.filter(user=self.request.user).order_by('-created_at')
        return eljus

class ProblemDetailView(LoginRequiredMixin, generic.DetailView):
    model = ProblemManage
    template_name = 'problem_detail.html'

# class ProblemCreateView(LoginRequiredMixin, generic.CreateView):
#     model = ProblemManage
#     template_name = 'problem_create.html'
#     form_class = ProblemCreateForm
#     success_url = reverse_lazy('problem:problem_create')

#     def form_valid(self, form):
#         diary = form.save(commit=False)
#         diary.user = self.request.user
#         diary.save()
#         messages.success(self.request, '日記を作成しました。')
#         return super().form_valid(form)

#     def form_invalid(self, form):
#         messages.error(self.request, "日記の作成に失敗しました。")
#         return super().form_invalid(form)