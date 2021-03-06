import re
from django.contrib import messages
from django.http import HttpResponseRedirect


class ImageField404Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if (request.method == 'POST' and request.user.is_superuser and response.status_code == 302 and request.get_full_path().startswith('/admin/')):

            post_messages = messages.get_messages(request)
            for message in post_messages:
                if ('was added successfully' in message.message or 'was changed successfully' in message.message and message.level == messages.SUCCESS):
                    messages.success(request, message.message)
                    redirect_url = request.get_full_path()
                    if '_addanother' in request.POST:
                        redirect_url = re.sub(
                            r'[^/]*/[^/]*/$', 'add/', redirect_url)
                    elif '_save' in request.POST:
                        redirect_url = re.sub(
                            r'[^/]*/[^/]*/(\?.*)?$', '', redirect_url)
                        if '_changelist_filters' in request.GET:
                            preserved_filters = parse.parse_qsl(
                                request.GET['_changelist_filters'])
                            redirect_url = + '?' + \
                                parse.urlencode(preserved_filters)
                    elif '_continue' in request.POST:
                        redirect_url_search = re.search(
                            r'((?<=href=>)[^>]*)', message.message)
                        if redirect_url_search:
                            redirect_url = redirect_url_search.group(0)

                            redirect_url = re.sub(
                                r'[\\"]*', '', redirect_url).replace('/admin/admin/', '/admin/')
                    return HttpResponseRedirect(redirect_url)
        return response
