from django.apps import AppConfig
from emoji import emojize

class BlogConfig(AppConfig):
    name = 'blog'

    def ready(self):
        print(emojize(':pear:') * 50)
        print('$$$$$$$$$$$$use ready function in Apps.py to run one time script at startup of application$$$$$$$$$$$$')
        print('$$$$$$$$$$$$use ready function in Apps.py to run one time script at startup of application$$$$$$$$$$$$')
        print('$$$$$$$$$$$$use ready function in Apps.py to run one time script at startup of application$$$$$$$$$$$$')
        print('$$$$$$$$$$$$use ready function in Apps.py to run one time script at startup of application$$$$$$$$$$$$')
        print(emojize(':thumbs_up:') * 50)
