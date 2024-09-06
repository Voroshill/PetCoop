from django.contrib import admin

from .models import User, UserCategory, Project, Language, News

admin.site.register(User)
admin.site.register(UserCategory)
admin.site.register(Project)
admin.site.register(Language)
admin.site.register(News)


