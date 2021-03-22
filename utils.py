from urllib.parse import urlparse

from django.urls import resolve, Resolver404

from activitylogs.constants import PAGES


def get_from_page(request):
    referer = request.META.get('HTTP_REFERER', None)
    if referer:
        try:
            url_parse = urlparse(referer)
            url_name = resolve(url_parse.path).url_name
            url_namespace = resolve(url_parse.path).namespace
            if url_namespace in ('events', 'training-events'):
                url_name = f'{url_namespace}:{url_name}'

            return PAGES.get(url_name, None)
        except Resolver404:
            pass

    return referer if referer and isinstance(referer, str) else 'Other source'
