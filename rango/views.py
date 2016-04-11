from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone


def index(request):
    template = loader.get_template('rango/index.html')
    context = {
        'boldmessage': "I am bold font from the context"
    }
    return HttpResponse(template.render(context, request))

"""
def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('rango/index.html', context_dict, context)
    #return HttpResponse("Rango says there you are! <a href='/rango/about'>About</a>")
"""


def about(request):
    #return HttpResponse("Rango says: there your about page <a href='/rango/'>Home</a>")
    template = loader.get_template('rango/about.html')
    context = {
        'boldmessage': "I am bold font from the context"
    }
    return HttpResponse(template.render(context, request))
