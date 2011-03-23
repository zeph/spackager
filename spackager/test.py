#-*- coding:utf-8 -*-
#
# Copyright (C) 2008 - Olivier Lauzanne <olauzanne@gmail.com>
#
# Distributed under the BSD license, see LICENSE.txt
from webob import Request, Response, exc
from lxml import etree
import unittest
import doctest
import httplib
import socket
import os

import pyquery
from pyquery import PyQuery as pq
from pyquery.ajax import PyQuery as pqa

import spackager
from spackager.spa import compile, _get_uri

socket.setdefaulttimeout(1)

try:
    conn = httplib.HTTPConnection("pyquery.org:80")
    conn.request("GET", "/")
    response = conn.getresponse()
except (socket.timeout, socket.error):
    GOT_NET=False
else:
    GOT_NET=True

def with_net(func):
    if GOT_NET:
        return func

dirname = os.path.dirname(os.path.abspath(spackager.__file__))
docs = os.path.join(os.path.dirname(dirname), 'docs')
path_to_html_file = os.path.join(dirname, 'test.html')

def input_app(environ, start_response):
    resp = Response()
    req = Request(environ)
    if req.path_info == '/':
        resp.body = '<input name="youyou" type="text" value="" />'
    elif req.path_info == '/submit':
        resp.body = '<input type="submit" value="OK" />'
    else:
        resp.body = ''
    return resp(environ, start_response)

class TestWebPackager(unittest.TestCase):
    @with_net
    def test_get(self):
        d = pq('http://guidoserra.it/')

if __name__ == '__main__':
    fails, total = unittest.main()
    if fails == 0:
        print 'OK'
