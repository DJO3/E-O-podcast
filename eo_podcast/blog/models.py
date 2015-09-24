from django.db import models


# Tags to accompany each Entry
class Tags(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Blog Posts
class Entry(models.Model):
    title = models.CharField(max_length=140, unique=True)
    body = models.TextField()
    url = models.SlugField(max_length=200, unique=True)
    published = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tags, related_name='entries')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

