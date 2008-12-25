from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_page

from faststart.app.models import *

def view1(request):

    context = RequestContext(request)

    context.update({
        'var1': "",
    })
    return render_to_response('app/appbase.html', context)

