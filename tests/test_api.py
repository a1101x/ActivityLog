import json

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from suppliers.factories import CompanyFactory

client = Client()


class ActivityLogViewTest(APITestCase):
    """
    Tests for:
    GET /api/activity-log-create/
    """

    def test_single_action(self):
        """
        POST /api/activity-log-create/
        """
        data = json.dumps({
            'action': 'share_by_email',
            'feature': 'share_by_email',
            'suppliers': []
        })
        response = client.post('/api/activity-log-create/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_multiple_actions(self):
        """
        POST /api/activity-log-create/
        """
        company1 = CompanyFactory()
        company2 = CompanyFactory()
        data = json.dumps({
            'action': 'share_by_email',
            'feature': 'share_by_email',
            'suppliers': [company1.id, company2.id]
        })
        response = client.post('/api/activity-log-create/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_contact_supplier(self):
        """
        POST /api/activity-log-create/
        """
        company1 = CompanyFactory()
        company2 = CompanyFactory()
        data = json.dumps({
            'action': 'contact_supplier',
            'feature': 'contact_supplier',
            'suppliers': [company1.id, company2.id],
            'supplier_contacts': {
                str(company1.id): ['test1@email.com', 'test2@email.com'],
                str(company2.id): ['test1@email.com', 'test2@email.com'],
            }
        })
        response = client.post('/api/activity-log-create/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_fe_supplier(self):
        """
        POST /api/activity-log-create/
        """
        company1 = CompanyFactory()
        data = json.dumps({
            'action': 'contact_supplier',
            'feature': 'contact_supplier',
            'supplier': company1.id,
            'supplier_contacts': {
                str(company1.id): ['test1@email.com', 'test2@email.com'],
            }
        })
        response = client.post('/api/activity-log-create/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
