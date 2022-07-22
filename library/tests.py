from django.test import TestCase
from rest_framework.test import APIClient

# Django doesn't use PyTest --> It has all the necessary API's inbuilt

# Create your tests here. (UnitTest Framework)

# class HelperClassTestCase(TestCase):
#
#     def test_when_trying_to_register_user_with_existing_fail(self):
#         raise NotImplemented


class BookViewTestCase(TestCase):

    def setUp(self): # Prepare for the test
        pass

    def test_get_book2_with_invalid_data_return_422(self):
        client = APIClient()
        result = client.post('/books2', None)
        self.assertEqual(result.status_code, 422)

    def tearDown(self): # Empty the test
        pass


