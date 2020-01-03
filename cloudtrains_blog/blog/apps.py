from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'

    def ready(self):
        print('$$$$$$$$$$$$use ready function in Apps.py to run one time script at startup of application$$$$$$$$$$$$')
        print('$$$$$$$$$$$$use ready function in Apps.py to run one time script at startup of application$$$$$$$$$$$$')
        print('$$$$$$$$$$$$use ready function in Apps.py to run one time script at startup of application$$$$$$$$$$$$')
        print('$$$$$$$$$$$$use ready function in Apps.py to run one time script at startup of application$$$$$$$$$$$$')