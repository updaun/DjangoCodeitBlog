from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    path('posts/', views.post_list, name='post-list'),
    # path('posts/new', view.post_create),
    path('posts/<int:post_id>/', views.post_detail, name='post-detail'),
    # path('posts/<int:post_id>/edit', view.post_update),
    # path('posts/<int:post_id>/delete', view.post_delete),
]   
