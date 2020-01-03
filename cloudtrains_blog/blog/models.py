from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'),
                      ('published', 'Published'),
                      )

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    deleted = models.BooleanField(default=False)
    delete_on = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.delete_on = timezone.now()
        self.deleted = True
        self.save()
