from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # post Views
    # function based view url
    # path('', views.post_list, name='post_list'),

    # class based view url
    # add this in pagination html  page=page_obj
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),

]
