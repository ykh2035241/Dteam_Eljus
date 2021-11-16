from django.shortcuts import render

from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import ProblemCreateForm #p271 1116
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
        eljus = ProblemManage.objects.filter(username=self.request.user).order_by('-created_at')
        return eljus

class ProblemDetailView(LoginRequiredMixin, generic.DetailView):
    model = ProblemManage
    template_name = 'problem_detail.html'

class ProblemCreateView(LoginRequiredMixin, generic.CreateView):
    model = ProblemManage
    template_name = 'problem_create.html'
    form_class = ProblemCreateForm
    success_url = reverse_lazy('problem:problem_create')

    def form_valid(self, form):
        diary = form.save(commit=False)
        diary.user = self.request.user
        diary.save()
        messages.success(self.request, '日記を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "日記の作成に失敗しました。")
        return super().form_invalid(form)

class ProblemUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = ProblemManage
    template_name = 'problem_update.html'
    form_class = ProblemCreateForm

    def get_success_url(self):
        return reverse_lazy('eljus:problem_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '日記を更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "日記の更新に失敗しました。")
        return super().form_invalid(form)

# class DiaryDeleteView(LoginRequiredMixin, generic.DeleteView):
#     model = Diary
#     template_name = 'diary_delete.html'
#     success_url = reverse_lazy('diary:diary_list')

#     def delete(self, request, *args, **kwargs):
#         messages.success(self.request, "日記を削除しました。")
#         return super().delete(request, *args, **kwargs)
