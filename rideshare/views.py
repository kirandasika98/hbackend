# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    '''
    A place holder index view for django
    '''
    print request
    return HttpResponse("Rideshare.",
                        content_type="application/json")