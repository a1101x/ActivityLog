from datetime import datetime, timedelta
from uuid import uuid4

from django_user_agents.utils import get_user_agent
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.functional import SimpleLazyObject

from activitylogs.activity_log import ActivityLog
from activitylogs.constants import ActionTypes, DeviceTypes
from activitylogs.utils import get_from_page
from users.models import UserBuyer, UserSupplier

User = get_user_model()


class ActivityLogMiddleware(object):

    def __init__(self, get_response=None):
        if get_response is not None:
            self.get_response = get_response

        super().__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response

    def _get_device_type(self, user_agent):
        device_type = DeviceTypes.UNKNOWN

        try:
            devices = {
                DeviceTypes.MOBILE: user_agent.is_mobile,
                DeviceTypes.TABLET: user_agent.is_tablet,
                DeviceTypes.DESKTOP: user_agent.is_pc,
                DeviceTypes.BOT: user_agent.is_bot,
            }

            device_type = [k for k, v in devices.items() if v][0]
        except (AttributeError, IndexError, KeyError, TypeError):
            pass

        return device_type

    def _get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR', None)

        return ip

    def _get_referrer(self, request):
        return request.COOKIES.get('Referrer', None)

    def is_search(self, request):
        return 'q' in getattr(request, 'GET', [])

    def _get_search_data(self, request, log):
        def get_action(request):
            if 'public_lists' in request.path:
                action = ActionTypes.SEARCH_PUBLIC_SAVED_LIST
            elif 'opportunities' in request.path:
                action = ActionTypes.SEARCH_OPPORTUNITY
            elif request.GET.get('catalog', None) in settings.OFFERINGS_CLASSIFICATORS:
                action = ActionTypes.SEARCH_COMMODITY_CODES
            elif request.GET.get('catalog', None) in settings.CODE_CLASSIFICATORS:
                action = ActionTypes.SEARCH_CONTRACT_VEHICLES
            else:
                action = ActionTypes.MAIN_SEARCH

            return action

        if request.GET.get('q', None) or request.GET.get('name_q', None):
            log = log._replace_data(
                search_query=request.GET.get('q', None) or request.GET.get('name_q', None),
                search_catalog=request.GET.get('catalog', None),
                search_section=request.GET.get('section', None),
                action=get_action(request),
            )

        return log

    def _get_user_organization(self, user):
        try:
            company_id = user.organization.id
            company_name = user.organization.name
        except (AttributeError, UserBuyer.DoesNotExist, UserSupplier.DoesNotExist):
            return None, None

        return company_id, company_name

    def _get_user_subscription(self, user):
        if user.is_supplier:
            try:
                account = user.profile.organization.payment_accounts.first()
                if account:
                    subscription = account.account_subscriptions.active().first()
                    return subscription.plan.level.name if subscription else 'Free'
            except (AttributeError, UserBuyer.DoesNotExist, UserSupplier.DoesNotExist):
                pass

            return 'Free'

        return None

    def _get_page_url(self, request):
        return f'{settings.SERVER_SCHEMA}://{settings.SERVER_DOMAIN}{request.path}'

    def _get_device_id(self, request):
        return request.COOKIES.get('gDeviceId', None)

    def process_request(self, request):
        user_agent = SimpleLazyObject(lambda: get_user_agent(request))
        user = request.user if hasattr(request, 'user') else None
        user_id = None
        user_name = None
        user_email = None
        user_type = None
        user_date_joined = None
        company_id = None
        company_name = None
        subscription = None

        if user is not None and not user.is_anonymous and user.is_authenticated:
            user_id = user.id
            user_name = user.get_full_name()
            user_email = user.email
            user_type = User.USER_TYPES[user.user_type]
            user_date_joined = user.date_joined
            company_id, company_name = self._get_user_organization(user)
            subscription = self._get_user_subscription(user)

        log = ActivityLog(
            company_id=company_id,
            company_name=company_name,
            device_id=self._get_device_id(request),
            ip=self._get_client_ip(request),
            page_url=self._get_page_url(request),
            page=get_from_page(request),
            referrer=self._get_referrer(request),
            subscription=subscription,
            user_id=user_id,
            user_name=user_name,
            user_email=user_email,
            user_type=user_type if user_type else 'Not registered',
            user_date_joined=user_date_joined,
        )

        if self.is_search(request):
            log = self._get_search_data(request, log)

        try:
            log = log._replace_data(
                browser=user_agent.browser.family,
                device_type=self._get_device_type(user_agent),
                device=user_agent.device.family,
                os_version=user_agent.os.version_string,
                os=user_agent.os.family,
            )
        except TypeError:
            pass


        request.activity_log = log
        request.device_id = self._get_device_id(request)

    def process_response(self, request, response):
        # set unique id for a connected device (browser)
        if not request.COOKIES.get('gDeviceId'):
            one_year = datetime.now() + timedelta(days=365)
            expires = datetime.strftime(one_year, '%a, %d-%b-%Y %H:%M:%S GMT')
            response.set_cookie('gDeviceId', uuid4(), expires=expires)

        ref_type = request.GET.get('ref', None)
        if ref_type:
            response.set_cookie('Referrer', ref_type)

        return response
