"""
Unit test for the controller.

Goal: verify the DELETE endpoint returns 200 OK and the account
is actually removed. We mock nothing here — it's a simple,
standard integration-style unit test using DRF's test client.
"""

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Account


class DeleteAccountViewTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        # Create a test account to delete
        self.account = Account.objects.create(name="Test User")

    def test_delete_account_returns_200(self):
        url = f"/accounts/{self.account.id}"
        response = self.client.delete(url)

        # Assert HTTP 200 OK as required
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert the account no longer exists in DB
        self.assertFalse(Account.objects.filter(id=self.account.id).exists())

    def test_delete_nonexistent_account_returns_404(self):
        response = self.client.delete("/accounts/9999")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)   