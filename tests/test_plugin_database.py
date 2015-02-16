#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
==================================
Test the database plugin
==================================
"""
from __future__ import unicode_literals

import unittest

import mongomock
from irc3.testing import BotTestCase, patch


class DatabasePluginTest(BotTestCase):

    config = {
        'includes': ['onebot.plugins.database'],
        'cmd': '!',
        'onebot.plugins.database': {
            'host': 'thehost',
            'port': 1234
        }
    }

    @patch('pymongo.MongoClient', mongomock.MongoClient)
    def setUp(self):
        self.callFTU()

    def test_getattr(self):
        assert isinstance(self.bot.get_database().users, mongomock.Collection)

    def test_get_database(self):
        assert isinstance(self.bot.get_database(), mongomock.Database)


if __name__ == '__main__':
    unittest.main()