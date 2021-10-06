from django.test import TestCase
from .models import UserInfo
from django.urls import reverse

# Create your tests here.

class UserInfoModelTest(TestCase):
    def setUp(self):
        self.userInfo=UserInfo.objects.create(first_name="anjali",last_name="vats",email="anj@gmail.com",phone="3453543")
    def test_UserInfo_contents(self):
        self.assertEqual(f"{self.userInfo.first_name}","anjali")
        self.assertEqual(f"{self.userInfo.last_name}","vats")
        self.assertEqual(f"{self.userInfo.email}","anj@gmail.com")
        self.assertEqual(f"{self.userInfo.phone}","3453543")


class HomepageViewTest(TestCase):
    def test_homepage_at_correct_location(self):
        resp=self.client.get('/')
        self.assertEqual(resp.status_code,200)
    def test_homepage_by_name(self):
        resp=self.client.get(reverse("home"))
        self.assertEqual(resp.status_code,200)
    def test_url_uses_correct_template(self):
        resp=self.client.get(reverse("home"))
        self.assertEqual(resp.status_code,200)


class aboutpageViewTest(TestCase):
    def test_aboutpage_at_correct_location(self):
        resp=self.client.get('/about')
        self.assertEqual(resp.status_code,200)
    def test_aboutpage_by_name(self):
        resp=self.client.get(reverse("about"))
        self.assertEqual(resp.status_code,200)
    def test_url_uses_correct_template(self):
        resp=self.client.get(reverse("about"))
        self.assertEqual(resp.status_code,200)

    