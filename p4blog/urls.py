from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('edit_post/<slug:slug>', views.EditPostView.as_view(), name='edit_post'),
]