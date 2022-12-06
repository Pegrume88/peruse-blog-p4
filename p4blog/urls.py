from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    path('edit_post/<slug:slug>', views.EditPostView.as_view(), name='edit_post'),
    path('delete_post/<slug:slug>/remove', views.DeleteView.as_view(), name='delete_post'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('category_view/', views.CategoryView.as_view(), name='category'),
]