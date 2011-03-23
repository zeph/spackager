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
uri = 'http://guidoserra.it'
filename = 'run.html'

try:
    conn = httplib.HTTPConnection("pyquery.org:80")
    conn.request("GET", "/")
    response = conn.getresponse()
except (socket.timeout, socket.error):
    GOT_NET=False
else:
    GOT_NET=True

class TestWebPackager(unittest.TestCase):
    def test_spac(self):
        original = _get_uri(uri)
        html = compile(original, False)
        outfile = filename.replace('.html', '.mhtml')
        f = open(outfile, 'w')
        f.write(html)
        f.close()

if __name__ == '__main__':
    fails, total = unittest.main()
    if fails == 0:
        print 'OK'
