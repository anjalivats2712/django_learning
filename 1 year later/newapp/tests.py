from django.test import TestCase,SimpleTestCase


# Create your tests here.
class SimpleTests(SimpleTestCase):
    def test_home_status_code_check(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code,200)
    def test_contact_status_code_check(self):
        response2=self.client.get('/contact')
        self.assertEqual(response2.status_code,200)