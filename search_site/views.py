from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string
from rest_framework import generics
from .models import User, News
from .serializers import UserSerializer

menu = [{'title': "News", 'url_name': 'news'},
        {'title': "Search", 'url_name': 'search'},
        {'title': "Projects", 'url_name': 'projects'},
        {'title': "Topics", 'url_name': 'topics'},
        {'title': 'About', 'url_name': 'about'},
        ]


class PetCoopAPI(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def mainpage(request):
    data = {'title': "Mainpage",
            'menu': menu,
            }
    return render(request, 'search_site/mainpage.html', data)


def news(request):
    news = News.objects.all()
    data = {'menu': menu,
            'news': news,
            }
    return render(request, 'search_site/news.html', data)


def show_news(request, slug):
    return HttpResponse(f"Reading the article with slug - {slug}")


def search(request):
    data = {'title': "Search",
            'menu': menu,
            }
    return render(request, 'search_site/search.html', data)


def projects(request):
    data = {'title': "Projects",
            'menu': menu,
            }
    return render(request, 'search_site/projects.html', data)


def topics(request):
    data = {'title': "Topics",
            'menu': menu,
            }
    return render(request, 'search_site/topics.html', data)


def about(request):
    return render(request, 'search_site/about.html', {"title": "About", 'menu': menu})


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
