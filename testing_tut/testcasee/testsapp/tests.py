from django.test import TestCase,SimpleTestCase
from .models import Post,Info
from django.urls import reverse

# Create your tests here.
class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text="just a text")

    def test_text_content(self):
        post=Post.objects.get(id=1)
        expected_object_text=f"{post.text}"
        self.assertEqual(expected_object_text,"just a text")
        

class InfoModelTest(TestCase):
    def setUp(self):
        self.info=Info.objects.create(name="kartik",email="anj@gmail.com",phone="9467892312")
    def test_info_content(self):
        self.assertEqual(f"{self.info.name}","kartik")
        self.assertEqual(f"{self.info.email}","anj@gmail.com")
        self.assertEqual(f"{self.info.phone}","9467892312")
    
class HomePageView(TestCase):
    def setUp(self):
        Post.objects.create(text = "another text")
    def test_view_url_at_proper_location(self):
        resp=self.client.get("/")
        self.assertEqual(resp.status_code,200)
    def test_view_url_by_name(self):
        resp=self.client.get(reverse("home"))
        self.assertEqual(resp.status_code,200)

    def test_view_uses_correct_template(self):
        resp=self.client.get(reverse("home"))
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp,"home.htm")

class AboutPageView(SimpleTestCase):
    def test_about_page_status(self):
        response=self.client.get('/about')
        self.assertEqual(response.status_code,200)
    def test_view_url_by_name(self):
        resp=self.client.get(reverse("about"))
        self.assertEqual(resp.status_code,200)
    def test_url_uses_correct_template(self):
        resp=self.client.get(reverse("about"))
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp,"about.htm")



