from django.test import TestCase
from .models import Profile, Image, User, Comments

# Create your tests here.
class ProfileTest(TestCase):

    def setUp(self):
        self.new_user = User(username='kim', email='kim@gmail.com', password='1234')
        self.new_user.save()
        self.new_profile = Profile(profile_image='kim.png', bio='kim', user=self.new_user)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    def test_save_method(self):
        self.new_profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)
    
   # Create your tests here.
class ImageTest(TestCase):

    def setUp(self):
        self.new_user = User(username='kim', email='kim@gmail.com', password='1245')
        self.new_user.save()
        self.new_profile = Profile(profile_image='kim.jpg', bio='give', user=self.new_user)
        self.new_profile.save()
        self.new_image = Image(image_name='dust', image='yes.jpg', image_caption='dust', profile=self.new_user)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))

    def test_save_image(self):
        self.new_image.save_image()
        image = Image.objects.all()
        self.assertTrue(len(image)>0)

    

class CommentsTest(TestCase):

    def setUp(self):
        self.new_user = User(username='kim', email='kim@gmail.com', password='1234')
        self.new_user.save()
        self.new_image = Image(image_name='lion', image='lion.jpg', image_caption='lionwhite', profile=self.new_user)
        self.new_image.save()
        self.new_comment = Comments(comment='wildlife',image=self.new_image,user=self.new_user)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comments))

    def test_save_comment(self):
        self.new_comment.save_comment()
        comment = Comments.objects.all()
        self.assertTrue(len(comment)>0)


