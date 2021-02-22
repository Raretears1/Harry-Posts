from django.urls import path

from . import views

urlpatterns = [
    path('posts/', views.PostsListView.as_view(), name='posts'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post'),
    path('posts/create', views.PostCreateView.as_view(), name='create_post'),
    path('post', views.PostCreateView.as_view(), name='comment')
]
