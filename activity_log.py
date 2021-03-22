import re
from datetime import datetime
from typing import NamedTuple

camel_case_pattern = re.compile('[^A-Za-z]+')


class ActivityLog(NamedTuple):
    action: str = None
    browser: str = None
    cc_id: int = None
    cc_name: str = None
    company_id: int = None
    company_name: str = None
    content_id: int = None
    content_name: str = None
    covid_supply_created_by: int = None
    covid_supply_id: int = None
    cv_id: int = None
    cv_name: str = None
    data_type: str = None
    device_id: str = None
    device_type: str = None
    device: str = None
    filter_id: int = None
    filter_name: str = None
    filter_options: list = None
    from_section: str = None
    ip: str = None
    items_num: int = None
    items_type: str = None
    num_of_suppliers: int = None
    opportunity_id: int = None
    opportunity_name: str = None
    opportunity_slug: str = None
    os_version: str = None
    os: str = None
    page_url: str = None
    page: str = None
    referrer: str = None
    saved_list_id: int = None
    saved_list_name: str = None
    search_catalog: str = None
    search_query: str = None
    search_section: str = None
    section: str = None
    shared: str = None
    subscription: str = None
    supplier_contacts: list = None
    supplier_id: int = None
    supplier_name: str = None
    supplier_section: str = None
    training_event_id: str = None
    training_event_name: str = None
    user_date_joined: datetime = None
    user_email: str = None
    user_id: int = None
    user_name: str = None
    user_request: str = None
    user_type: str = None
    what_was_clicked: str = None
    view_mode: str = None

    def camel(self, chars):
        words = camel_case_pattern.split(chars)
        return ''.join(w.lower() if i is 0 else w.title() for i, w in enumerate(words))

    def _replace_data(self, **kwargs):
        for k, v in kwargs.items():
            self = self._replace(**{k: v})

        return self

    def _to_dict(self, **kwargs):
        if kwargs:
            self = self._replace_data(**kwargs)

        return {
            self.camel(field): getattr(self, field)
            for field in self._fields
            if getattr(self, field, None) is not None
        }
