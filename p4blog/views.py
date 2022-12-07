from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Category
from .forms import CommentForm, PostForm
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class SignupView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('login')


class PostList(generic.ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 6


class CategoryList(generic.ListView):
    model = Category
    template_name = 'category_view.html'
    

    

    


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




#def CategoryView(request, cat):

    #category_view = Post.objects.filter(category=cat)
    #return render(request, 'category_view.html', {'cat': cat})
    


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

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




