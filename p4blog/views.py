from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from .models import Post, Category, Profile
from .forms import CommentForm, PostForm, NewSignUpForm, EditProfileForm, ChangePasswordForm
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class SignUpForm(generic.CreateView):
    form_class = NewSignUpForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('login')


class EditProfileView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class ChangePasswordView(PasswordChangeView):
    form_class = ChangePasswordForm
    success_url = reverse_lazy('home')


class PostList(generic.ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 6

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(PostList, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        
        return context



class AddPostView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    summernote_fields = 'content'
    # fields = ('title', 'author', 'content', 'featured_image')


class EditPostView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'edit_post.html'
    # fields = ('title', 'content', 'featured_image')
    summernote_fields = 'content'


class DeleteView(generic.DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class AddCategoryView(generic.CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'


def CategoryView(request, id):
    category_menu = Category.objects.all()

    category_posts = Post.objects.filter(category__pk=id)
    if len(category_posts) > 0:
        category_name = category_posts[0].category.name
    else:
        category_name = ''
   
    return render(request, 'category_view.html', {'cats':category_name, 'category_posts':category_posts, 'category_menu':category_menu})
    

class PostDetail(View):


    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = True
        if post.likes.filter(id=self.request.user.id).exists():
            liked = False

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )




