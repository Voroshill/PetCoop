from django.contrib import admin

from .models import User, UserCategory, Project, Language, News

admin.site.register(User)
admin.site.register(UserCategory)
admin.register(Project)
admin.register(Language)
admin.register(News)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_programming_language', 'author', 'tags', 'is_visible']
    list_filter = ['programming_language__name', 'author', 'is_visible', 'time_created', 'time_updated']
    search_fields = ['name', 'author__username', 'description', 'tags', 'programming_language__name']
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ['author']
    date_hierarchy = 'time_created'

    def get_programming_language(self, obj):
        return obj.programming_language.name
    get_programming_language.short_description = 'Programming Language'


@admin.register(News)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'tags', 'published']
    list_filter = ['published', 'time_created', 'time_updated']
    search_fields = ['name', 'author', 'description', 'tags']
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ['author']
    date_hierarchy = 'time_created'
