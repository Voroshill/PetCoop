from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.urls import reverse




class User(models.Model):
    """Public Data"""
    nickname = models.CharField(unique=True, max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name='Slug', validators=[
            MinLengthValidator(5, message='Min 5 symbols'),
            MaxLengthValidator(20, message='Max 20 symbols'),
        ])
    image = models.FileField(blank=True, upload_to='users_images/')
    age = models.IntegerField()
    country = models.CharField(max_length=30)
    programming_language = models.ForeignKey("Language", on_delete=models.PROTECT, null=True)

    frameworks = models.CharField(max_length=255)
    experience = models.BigIntegerField(blank=True)
    about_me = models.CharField(blank=True, max_length=255)

    '''Private Data for site's modules and apps'''
    email = models.EmailField(blank=True)
    usertype = models.ForeignKey('UserCategory', on_delete=models.PROTECT, null=True)
    time_created = models.DateTimeField(blank=True,
                                        auto_now_add=True)
    time_updated = models.DateTimeField(blank=True, auto_now=True)
    last_visited = models.DateTimeField(blank=True, auto_now=False)
    visible = models.BooleanField(blank=True,
                                  default=False)
    is_online = models.BooleanField(blank=True, default=False)
    confirmation = models.BooleanField(blank=True, default=False)


class UserCategory(models.Model):
    name = models.CharField(max_length=20, db_index=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Hide'
        PUBLISHED = 1, 'Visible'

    name = models.CharField(max_length=40, db_index=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='Slug', validators=[
        MaxLengthValidator(50, message='Max 50 symbols'),
    ])
    programming_language = models.ForeignKey("Language", on_delete=models.PROTECT, null=True)
    description = models.TextField()
    tags = models.CharField(blank=True, max_length=255)
    author = models.ForeignKey("User", default='Hidden', on_delete=models.CASCADE, null=True, related_name='project_post')
    is_visible = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                     default=Status.DRAFT, verbose_name='Status')
    time_created = models.DateTimeField(blank=True, auto_now_add=True)
    time_updated = models.DateTimeField(blank=True, auto_now=True)


class Language(models.Model):
    name = models.CharField(max_length=20, unique=True, db_index=True)
    slug = models.SlugField(max_length=20, unique=True, db_index=True, verbose_name='Slug',
                            validators=[
                                MaxLengthValidator(20, message='Max 20 symbols'),
                            ])


class News(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, db_index=True)
    description = models.TextField()
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='Slug', validators=[
        MaxLengthValidator(50, message='Max 50 symbols'),
    ])
    tags = models.CharField(blank=True, max_length=255)
    published = models.BooleanField(default=False)
    time_created = models.DateTimeField(blank=True, auto_now_add=True)
    time_updated = models.DateTimeField(blank=True, auto_now=True)
    author = models.ForeignKey("User", default='Hidden', on_delete=models.CASCADE, null=True, related_name='news_post')
    objects = models.Manager()
    published_news = PublisherManager()

    class Meta:
        ordering = ['-time_created']
        indexes = [
            models.Index(fields=['time_created'])
        ]
