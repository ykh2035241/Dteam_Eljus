from django.urls import path

from . import views

app_name = 'eljus'
urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),

    path('home/',views.HomeView.as_view(),name="home"),

    path('problem-list/',views.ProblemListView.as_view(),name="problem_list"),#p244 1112
    path('problem-detail/<int:pk>/', views.ProblemDetailView.as_view(), name="problem_detail"),
    path('problem-create/',views.ProblemCreateView.as_view(),name="problem_create"),#p269 1116
    path('problem-update/<int:pk>/',views.ProblemUpdateView.as_view(),name="problem_update"),#p275 1116
]