from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager

# Create Custom Model Manager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

    # Create your models here.


class Post(models.Model):
    tag = TaggableManager()
    objects = models.Manager()  # default Manager
    published = PublishedManager()  # Custom Manager

    # Canonical url

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])

    STATUS_CHOICES = (('draft', 'Draft'),
                      ('published', 'Published'),
                      )

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
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


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on  {}'.format(self.name, self.post)


