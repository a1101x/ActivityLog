import re

snake_case_pattern = re.compile(r'(?<!^)(?=[A-Z])')

PROPERTIES_MAPPING = {
    'action': 'event_type',
    'browser': 'event_properties',
    'ccId': 'event_properties',
    'ccName': 'event_properties',
    'companyId': 'user_properties',
    'companyName': 'user_properties',
    'contentId': 'event_properties',
    'contentName': 'event_properties',
    'covidSupplyCreatedBy': 'event_properties',
    'covidSupplyId': 'event_properties',
    'cvId': 'event_properties',
    'cvName': 'event_properties',
    'deviceId': 'device_id',
    'deviceType': 'platform',
    'device': 'device_model',
    'filterId': 'event_properties',
    'filterName': 'event_properties',
    'filterOptions': 'event_properties',
    'ip': 'ip',
    'itemsNum': 'event_properties',
    'itemsType': 'event_properties',
    'numOfSuppliers': 'event_properties',
    'opportunityId': 'event_properties',
    'opportunityName': 'event_properties',
    'opportunitySlug': 'event_properties',
    'osVersion': 'os_version',
    'os': 'os_name',
    'pageUrl': 'event_properties',
    'page': 'event_properties',
    'referrer': 'event_properties',
    'savedListId': 'event_properties',
    'savedListName': 'event_properties',
    'searchCatalog': 'event_properties',
    'searchQuery': 'event_properties',
    'searchSection': 'event_properties',
    'section': 'event_properties',
    'shared': 'event_properties',
    'subscription': 'event_properties',
    'supplierContacts': 'event_properties',
    'supplierId': 'event_properties',
    'supplierName': 'event_properties',
    'supplierSection': 'event_properties',
    'trainingEventId': 'event_properties',
    'userEmail': 'user_properties',
    'userId': 'user_id',
    'userName': 'user_properties',
    'userRequest': 'event_properties',
    'userType': 'user_properties',
    'viewMode': 'event_properties',
}


class AmplitudeProperties:
    """
    Prepare data for sending to amplitude.
    All properties here:
    https://developers.amplitude.com/docs/http-api-v2#properties-1
    """

    def to_dict(self, data):
        result = {
            'event_properties': {},
            'user_properties': {},
        }

        for k, v in data.items():
            if k in PROPERTIES_MAPPING.keys():
                value = PROPERTIES_MAPPING[k]
                if value in ('event_properties', 'user_properties'):
                    result[value].update({snake_case_pattern.sub('_', k).lower(): v})
                else:
                    result[value] = v

        return result


amplitude_properties = AmplitudeProperties()
