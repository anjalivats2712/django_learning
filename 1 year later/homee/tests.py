from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Post

# Create your tests here.

class PostTest(TestCase):
    def setUp(self):
        #self.user=get_user_model().objects.create_user(username='kartik',email="kartik@gmail.com",password="123456")
        self.post=Post.objects.create(title="autumn",author="kartik",content="sadha bahar")
    def test_string_representation(self):
        post=Post(title="nya_title")
        self.assertEqual(str(post),post.title)
    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(),"/post/1")
    def test_post_content(self):
        self.assertEqual(self.post.title,"autumn")
        self.assertEqual(self.post.author,"kartik")
        self.assertEqual(self.post.content,"sadha bahar")
    def test_list_view(self):
        response=self.client.get(reverse("home"))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'autumn')
        self.assertTemplateUsed(response,'home.html')
    def test_detail_view(self):
        response=self.client.get('/post/1')
        no_response=self.client.get('/post/10000')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,"kartik")
        self.assertTemplateUsed(response,"postdetail.html")
    def test_post_create_view(self):
        response=self.client.post(reverse("post_create"),{"title":"new_title","author":"new_author","content":"new_content"})
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"new_title")
        self.assertContains(response,"new_content")
        self.assertTemplateUsed(response,"postcreate.html")
    def test_post_update_view(self):
        response=self.client.post(reverse("post_update",args="1"),{"title":"updated_title","content":"updated_content"})
        self.assertEqual(response.status_code,302)
    def test_post_create_view(self):
        response=self.client.get(reverse("post_delete",args='1'))
        self.assertEqual(response.status_code,200)

