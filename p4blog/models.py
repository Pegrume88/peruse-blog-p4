from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse

from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


# category model
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('home')

# Blog post Model
class Post(models.Model):

    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=220)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="p4blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    likes = models.ManyToManyField(User, related_name='blog_likes')

    class Meta:
        ordering = ['-created_on']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')

    def number_of_likes(self):
        return self.likes.count()

# comment section model
class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"comment{self.body} by {self.name}"


# Profile page model 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_image = CloudinaryField('image', default='placeholder', null=True, blank=True)
    facebook_url = models.CharField(max_length=250, null=True, blank=True)
    instagram_url = models.CharField(max_length=250, null=True, blank=True)
    twitter_url = models.CharField(max_length=250, null=True, blank=True)
   
    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse('home')

    # creates user profile when user registers 
    def create_profile(instance, created, **kwargs): 
        if created: 
            Profile.objects.create(user=instance) 

    post_save.connect(create_profile, sender=User)
