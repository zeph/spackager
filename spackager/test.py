#-*- coding:utf-8 -*-
#
# Copyright (C) 2011 - Guido Serra aka Zeph <zeph@fsfe.org>
# -> based on the "pyquery" test suite from Oliver Lauzanne
#
# Distributed under the GPL license
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

class TestWebPackager(unittest.TestCase):
    def test_spac(self):
        original = _get_uri(uri)
        mhtml = compile(original, False)
        # at least it does something...
        self.assertNotEqual(original, mhtml)

if __name__ == '__main__':
    fails, total = unittest.main()
    if fails == 0:
        print 'OK'
