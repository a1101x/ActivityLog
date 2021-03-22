from django.test import TestCase

from activitylogs.tasks import amplitude_event_send
from activitylogs.amplitude.properties import amplitude_properties


class AmplitudeTest(TestCase):

    def test_properties(self):
        data = {
            'action': 'test',
            'browser': 'test',
            'ccId': 1,
            'ccName': 'test',
            'companyId': 1,
            'companyName': 'test',
            'contentId': 1,
            'contentName': 'test',
            'covidSupplyCreatedBy': 1,
            'covidSupplyId': 1,
            'cvId': 1,
            'cvName': 'test',
            'deviceId': 'test-test-test',
            'deviceType': 'test',
            'device': 'PC',
            'filterId': 1,
            'filterName': 'test',
            'filterOptions': 'test',
            'ip': '127.0.0.1',
            'itemsNum': 1,
            'itemsType': 'test',
            'numOfSuppliers': 1,
            'opportunityId': 1,
            'opportunityName': 'test',
            'opportunitySlug': 'test',
            'osVersion': '20',
            'os': 'Linux',
            'pageUrl': 'test.com/test',
            'page': 'test',
            'referrer': 'test',
            'savedListId': 1,
            'savedListName': 'test',
            'searchCatalog': 'test',
            'searchQuery': 'test',
            'searchSection': 'test',
            'section': 'test',
            'shared': 'test',
            'subscription': 'test',
            'supplierContacts': 'test',
            'supplierId': 1,
            'supplierName': 'test',
            'supplierSection': 'test',
            'trainingEventId': 1,
            'userEmail': 'test@email.com',
            'userId': 1,
            'userName': 'test',
            'userRequest': 'test',
            'userType': 'test',
            'viewMode': 'test',
        }
        properties = amplitude_properties.to_dict(data)
        self.assertEqual(properties['user_id'], data['userId'])
        self.assertEqual(properties['event_properties']['items_num'], data['itemsNum'])
        self.assertEqual(properties['event_type'], data['action'])

