#!/usr/bin/env python
# coding=utf-8
from django.http import HTTPResponse

def index(request):
    return HTTPResponse("index")

