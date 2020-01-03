## Cloud Train Blog - Shri Ganeshay Namah
# ------------------------------------------
##### Setup Instructions
##### --------------------------------------
pip install virtualenv

activate virtual environment environment

source cloudtrians-blog-env/bin/activate

pip install django

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
