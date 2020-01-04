# Performance Improvement
https://instagram-engineering.com/dismissing-python-garbage-collection-at-instagram-4dca40b29172
https://code.kiwi.com/memory-efficiency-of-parallel-io-operations-in-python-6e7d6c51905d
https://engineering.upside.com/a-beginners-guide-to-optimizing-pandas-code-for-speed-c09ef2c6a4d6
https://www.freecodecamp.org/news/an-a-z-of-useful-python-tricks-b467524ee747/
https://www.freecodecamp.org/news/how-to-visualize-the-central-limit-theorem-in-python-b619f5b00168/
gevent 
threadpoolexecutor

##### Great
----------------------------------
pip install emoji

print(emojize(":thumbs_up:"))

pip install geopy

pip install howdoi

pip install typing

pip install pyyaml


to make jsonapi:  
marshmallow_jsonapi


You want to plot graphs in the console?
pip install bashplotlib
from collections import OrderedDict, Counter

# Cloud Train Blog - Shri Ganeshay Namah
# ------------------------------------------
##### Setup Instructions
##### --------------------------------------
pip install virtualenv

activate virtual environment environment

source cloudtrians-blog-env/bin/activate

pip install django

pip install werkzeug //mandatory for django-extensions
pip install django-extensions


##### Check version of django
##### -------------------------------------------
import django.get_version()

Running server with dev setting

python manage.py runserver 127.0.0.1:8001 --settings=cloudtrains_blog.settings

python manage.py startapp blog


python manage.py makemigrations blog

Check the SQL which django to apply when migrating schema to database

python manage.py sqlmigrate blog 0001

python manage.py migrate


# Creating a superuser
python manage.py createsuperuser

# Working with QuerySet and managers
The Django Object-relational mapper is compatible with MySQL, PostgreSQL, SQLite, and Oracle. Remember that you can define the database of your project
in the DATABASES setting of your project's settings.py file. Django can work with multiple databases at a time, and you can program database routers to create custom routing schemes.

a.  **Finding a record using ORM**
* user = User.objects.get(username='admin')
* DoesNotExist, MultipleObjectsReturned exception

b. **Creating a record using ORM**
1. _Post.objects.create(title='One more post', slug='one-more-post', body='Post body.', author=user)_

2. _post = Post(title='Another Post', slug='another-post', body='Post Body', author=user)_
    _post.save_

c. **Updating a record using ORM**

    1.  _post.tite = "New Title"_
    2.  _post.save()_
    
    Post.objects.filter(publish__year=2017, author__username='admin')
    Post.objects.filter(publish__year=2017) .exclude(title__startswith='Why')
    Post.objects.order_by('-title')post = Post.objects.get(id=1)

d. **Deleting a record using ORM**

    post = Post.objects.get(id=1)
    post.delete()    
## Run Custom SQL on startup of application
1. Creating an empty migration
$ ./manage.py makemigrations blog --empty -n create_custom_index
```python # -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-17 17:35
 from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            "CREATE INDEX i_active_posts ON posts(id) WHERE active",
            "DROP INDEX i_active_posts"
        )
    ]

```


2. Second Method 

$ mkdir scripts
$ touch scripts/__init__.py
$ touch scripts/delete_all_questions.py
$ python manage.py runscript delete_all_questions


# Creating Customer model managers
```python
# Create Customer Model Manager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset() .filter(status='published')


# Create your models here.

class Post(models.Model):
    objects = models.Manager() # default Manager
    published = PublishedManager() # Custom Manager

```
Post.objects.filter(id=3).update(status='published')

# Show SQL Quering from QuerySet Object
```python
# first way
str(Post.objects.filter(id=3).query)

# Second way
from django.db import connection
print(connection.queries)
```

# View in django

```python
from django.urls import path
from . import views

# app name used to orgainize urls by app name
app_name = 'blog'
urlpatterns = [# post views
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
                    views.post_detail,
                    name='post_detail'),
]
```

# Auto-generate the models
$ python manage.py inspectdb

$ python manage.py inspectdb > models.py


# Canonical URLs for models
```python
from django.urls import reverse
class Post(models.Model):
# ...
def get_absolute_url(self):
    return reverse('blog:post_detail',
        args=[self.publish.year,
        self.publish.month,
        self.publish.day,
        self.slug])
```
# Templates
### Creating templates for your views

```text
templates/
       blog/
            base.html
            post/
                 list.html
                 detail.html
```

# Type checking in Python

```python

from typing import Dict , list
fullname:Dict[str, int] =  {"name": "Sudeep", "lastName":"Patel"}

 def fun(a:int) -> int:
     return a
from typing import Tuple

my_data: Tuple[str, int, float] = ("Adam", 10, 5.7)
from typing import List, Tuple
```

### Creating Alias to complex type

```python
LatLngVector = List[Tuple[float, float]]

points: LatLngVector = [
    (25.91375, -60.15503),
    (-11.01983, -166.48477),
    (-11.01983, -166.48477)
]

 ```
##### Running the Type Checker
pip install mypy

mypy test.py

# Using Class Based View


# For Peformance analysis
sudo apt install linux-tools
sudo apt install linux-tools-generic

# Creating forms with Django

Form : Allows you to build standard forms

ModelForm: Allows you to build forms tied to model instances

## Sending Email from Django


from django.core.mail import send_mail
send_mail('Django Mail', 'This is a test email','sudeep.tech.patel@gmail.com', ['sudeep.tech.patel@gmail.com'], fail_silently=False)



EMAIL_HOST = 'localhost'
EMAIL_PORT = '8999'

EMAIL_HOST_USER: Password for the SMTP server
EMAIL_HOST_PASSWORD Whether to use a TLS secure connection
EMAIL_USE_TLS Whether to use an implicit TLS secure in case SMTP server not available
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
**_send_mail('Django Mail', 'This is a test email','@gmail.com', ['@gmail.com'], fail_silently=False)_**


# Adding the Tagging Functionality

pip install django_taggit==0.22.2

```python
INSTALLED_APPS = [
# ...
'blog.apps.BlogConfig',
'taggit',
]

# add taggit in models.py

from taggit.managers import TaggableManager
class Post(models.Model):
# ...
tags = TaggableManager()

_# use below in shell to add tag to blog_
from blog.models import Post                                                                                                                  

post = Post.objects.get(id=1)                                                                                                                 
post.tag.add('spritiual', 'social', 'indian')                                                                                                 
post.tag.all()                                                                                                                                

```
python manage.py runserver_plus --print-sql





