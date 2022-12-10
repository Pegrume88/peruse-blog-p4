from django.test import TestCase
from .forms import PostForm


"""
Testing forms 
"""

class TestPostForm(TestCase):

    """
    Testing if postform works 
    """
    def test_title_is_required(self):
        """
        Test if form submits without title field
        """

        form = PostForm({
            'title': '',
            'author': 'test',
            'category': 'test',
            'content': 'test',
            'featured_image': 'test',

        })
        # Form should not be valid - title required
        self.assertFalse(form.is_valid())
        #self.assertIn('title', form.errors.keys())
        # Check error message is correct
        #self.assertEqual(
           # form.errors['title'][0], 'This field is required.')