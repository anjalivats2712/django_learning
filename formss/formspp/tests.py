from django.test import TestCase,Client
from .models import UserInfo,Post
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.

class UserInfoModelTest(TestCase):
    def setUp(self):
        self.userInfo=UserInfo.objects.create(first_name="anjali",last_name="vats",email="anj@gmail.com",phone="3453543")
    def test_UserInfo_contents(self):
        self.assertEqual(f"{self.userInfo.first_name}","anjali")
        self.assertEqual(f"{self.userInfo.last_name}","vats")
        self.assertEqual(f"{self.userInfo.email}","anj@gmail.com")
        self.assertEqual(f"{self.userInfo.phone}","3453543")

class PostModelTest(TestCase):
    def setUp(self):
        self.user=get_user_model().objects.create_user(username="anj27",email="anj@gmail.com",password="anjali")
        self.post=Post.objects.create(title="leejong",auther=self.user,body="ljs")

    def test_str_represtation(self):
        post=Post(title="leejong")
        self.assertEqual(str(post),"leejong")

    def test_post_content(self):
        self.assertEqual(f"{self.post.title}","leejong")
        self.assertEqual(f"{self.post.auther}","anj27")
        self.assertEqual(f"{self.post.body}","ljs")
    def test_post_list_view(self):
        resp=self.client.get(reverse("home"))
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp,"home.html")
        self.assertContains(resp,"leejong")
    def test_post_details_view(self):
        resp=self.client.get("/post/1")
        no_resp=self.client.get("/post/1000")
        self.assertEqual(resp.status_code,200)
        self.assertEqual(no_resp.status_code,404)
        self.assertTemplateUsed(resp,"detail.html")
        self.assertContains(resp,"ljs")
        

# class HomepageViewTest(TestCase):
#     def test_homepage_at_correct_location(self):
#         resp=self.client.get('/')
#         self.assertEqual(resp.status_code,200)
#     def test_homepage_by_name(self):
#         resp=self.client.get(reverse("home"))
#         self.assertEqual(resp.status_code,200)
#     def test_url_uses_correct_template(self):
#         resp=self.client.get(reverse("home"))
#         self.assertEqual(resp.status_code,200)
#         self.assertTemplateUsed(resp,"home.html")


# class aboutpageViewTest(TestCase):
#     def test_aboutpage_at_correct_location(self):
#         resp=self.client.get('/about')
#         self.assertEqual(resp.status_code,200)
#     def test_aboutpage_by_name(self):
#         resp=self.client.get(reverse("about"))
#         self.assertEqual(resp.status_code,200)
#     def test_url_uses_correct_template(self):
#         resp=self.client.get(reverse("about"))
#         self.assertEqual(resp.status_code,200)

    