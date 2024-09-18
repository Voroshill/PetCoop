from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import User, News, Project, Language

menu = [{'title': "News", 'url_name': 'news'},
        {'title': "Search", 'url_name': 'search'},
        {'title': "Projects", 'url_name': 'projects'},
        {'title': "Discussions", 'url_name': 'discussions'},
        {'title': 'About', 'url_name': 'about'},
        ]


def mainpage(request):
    languages = Language.objects.all()
    data = {'title': "Mainpage",
            'menu': menu,
            'languages': languages
            }
    return render(request, 'search_site/mainpage.html', data)


def generic_list(request, model, template_name):
    objects_list = model.objects.all()
    paginator = Paginator(objects_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    data = {'title': model.__name__,
            'objects': page,
            'menu': menu,
            'page': page
            }
    return render(request, template_name, data)


def projects_list(request):
    return generic_list(request, Project, 'search_site/projects_list.html')


def news_list(request):
    return generic_list(request, News, 'search_site/news_list.html')


def show_new(request, slug):
    new = get_object_or_404(News, slug=slug)
    data = {'menu': menu,
            'title': new.name,
            'new': new,
            'tags': new.tags,
            }
    return render(request, 'search_site/show_new.html', data)


def show_project(request, slug):
    project = get_object_or_404(Project, slug=slug)
    data = {'menu': menu,
            'title': project.name,
            'name': project.name,
            'programming_language': project.programming_language,
            'description': project.description,
            'tags': project.tags,
            }
    return render(request, 'search_site/show_project.html', data)


def search(request):
    data = {'title': "Search",
            'menu': menu,
            }
    return render(request, 'search_site/search.html', data)


def discussions(request):
    data = {'title': "Discussions",
            'menu': menu,
            }
    return render(request, 'search_site/discussions.html', data)


def about(request):
    return render(request, 'search_site/about.html', {"title": "About", 'menu': menu})


def login(request):
    return HttpResponse('login')


def page_not_found(request, exception):
    return render(request, '404.html', status=404)
