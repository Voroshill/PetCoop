from django.urls import path
from . import views


urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('news/', views.news_list, name='news'),
    path('news/<str:slug>/', views.show_new, name='show_new'),
    path('search/', views.search, name='search'),
    path('projects/', views.projects_list, name='projects'),
    path('projects/<str:slug>/', views.show_project, name='show_project'),
    path('discussions/', views.discussions, name='discussions'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
]

