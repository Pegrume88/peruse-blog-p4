from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    path('edit_profile/', views.EditProfileView.as_view(), name='edit_profile'),
    path('edit_post/<slug:slug>', views.EditPostView.as_view(), name='edit_post'),
    path('delete_post/<slug:slug>/remove', views.DeleteView.as_view(), name='delete_post'),
    path('signup/', views.SignUpForm.as_view(), name='signup'),
    path('password/', views.ChangePasswordView.as_view(template_name='account/password_change.html')),
    path('category_view/<int:id>/', views.CategoryView, name='category_view'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
]