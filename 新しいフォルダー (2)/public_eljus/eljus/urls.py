from django.urls import path

from . import views

app_name = 'eljus'
urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),

    path('home/',views.HomeView.as_view(),name="home"),

    path('eljus-list/',views.EljusListView.as_view(),name="eljus_list"),#p244 1112
]