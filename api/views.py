import logging

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from activitylogs.api.serializers import ActivityLogSerializer
from activitylogs.constants import FRONTEND_ACTIONS, MULTIPLE_SUPPLIERS, SINGLE_SUPPLIERS
from suppliers.models import Company

activity_log = logging.getLogger('activity_log')
SEARCH_ACTIONS = [
    'main_search_was_filled', 'recent_searches_was_clicked', 'search_type_button_was_clicked',
    'search_result_was_clicked',
]


class ActivityLogView(APIView):
    serializer_class = ActivityLogSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        action = serializer.data.get('action')
        feature = serializer.data.get('feature', '')
        supplier = serializer.data.get('supplier', None)
        suppliers = serializer.data.get('suppliers', None)
        supplier_contacts = serializer.data.get('supplier_contacts', None)
        log = serializer.data.get('log', {})
        self._log_action(action, feature, supplier, log, suppliers, supplier_contacts)
        return Response(status=status.HTTP_200_OK)

    def _log_action(self, action, feature, supplier, log, suppliers, supplier_contacts=None):
        """
        Arguments:
            action {str} -- log action, i.e. send_email
            feature {str} -- log feature, i.e. contact_supplier
            supplier {int} -- supplier on which the action performs
            log {dict} -- additional data for a log
            suppliers {list} -- list of suppliers, for group actions

        Keyword Arguments:
            supplier_contacts {dict} -- only for contact_supplier feature, contacts for all suppliers from the action (default: {None})
        """
        is_search = action in SEARCH_ACTIONS
        action = FRONTEND_ACTIONS.get(action)
        activity = self.request.activity_log._replace_data(**log)

        if suppliers:
            if len(suppliers) > 1:
                activity_log.info(feature, extra={**activity._to_dict(
                    action=action.get(MULTIPLE_SUPPLIERS), num_of_suppliers=len(suppliers)
                )})

            suppliers_qs = dict(Company.objects.only('id', 'name').filter(id__in=suppliers).values_list('id', 'name'))
            for supplier in suppliers:
                if feature == 'contact_supplier' and supplier_contacts:
                    activity = activity._replace_data(supplier_contacts=supplier_contacts.get(str(supplier)))
                activity_log.info(feature, extra={**activity._to_dict(
                    action=action.get(SINGLE_SUPPLIERS), supplier_id=supplier,
                    supplier_name=suppliers_qs.get(supplier, None)
                )})
        else:
            if supplier and supplier > 0:
                supplier_name = Company.objects.only('name').get(id=supplier).name
                activity = activity._replace_data(supplier_id=supplier, supplier_name=supplier_name)
            if feature == 'contact_supplier' and supplier_contacts:
                activity = activity._replace_data(supplier_contacts=supplier_contacts.get(str(supplier)))

            data = {**activity._to_dict(action=action.get(SINGLE_SUPPLIERS))}
            if is_search: data.update({'tags': 'search'})
            activity_log.info(feature, extra={**data})
