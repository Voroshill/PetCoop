from django.urls import path
from . import views


urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('news/', views.news, name='news'),
    path('news/<str:slug>/', views.show_news, name='news'),
    path('search/', views.search, name='search'),
    path('projects/', views.projects, name='projects'),
    path('topics/', views.topics, name='topics'),
    path('about/', views.about, name='about'),

]

