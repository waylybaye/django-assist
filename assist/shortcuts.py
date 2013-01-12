from django.utils import simplejson
from django.http import HttpResponse


def render_json(object):
    return HttpResponse(simplejson.dumps(object), 'application/json')
