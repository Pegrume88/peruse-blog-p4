from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import PostForm
from pathlib import Path
from .models import User, Category

"""
Testing forms 
"""
BASE_DIR = Path(__file__).resolve().parent.parent

class TestPostForm(TestCase):

    """
    Testing if postform works 
    """
    def test_title_is_required(self):
        """
        Test if form submits without title field
        """
        upload_file = open('p4blog/urls.py', 'rb')
        author = User(username="test", password="test12345")
        author.save()
        category = Category(name="test")
        category.save()
        form = PostForm({
            'author': author,
            'category': category,
            'content': 'test',
            'featured_image': SimpleUploadedFile(upload_file.name, upload_file.read()),

        })
        # Form should not be valid - title required
        
        self.assertFalse(form.is_valid())
        
        self.assertIn('title', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['title'][0], 'This field is required.')