from django.conf.urls import url
from . import views
from django.urls import include, path



urlpatterns = [

    path('', views.post_list, name='post_list'),
    #path('post/(?P<pk>\d+)/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    #re_path('post/(?P<pk>\d+)/', views.post_detail, name='post_detail'),
    #re_path('post/new/', views.post_new, name='post_new'),
    #re_path('post/(?P<pk>\d+)/edit/', views.post_edit, name='post_edit'),

]
