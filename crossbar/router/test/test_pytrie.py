#####################################################################################
#
#  Copyright (C) Tavendo GmbH
#
#  Unless a separate license agreement exists between you and Tavendo GmbH (e.g. you
#  have purchased a commercial license), the license terms below apply.
#
#  Should you enter into a separate license agreement after having received a copy of
#  this software, then the terms of such license agreement replace the terms below at
#  the time at which such license agreement becomes effective.
#
#  In case a separate license agreement ends, and such agreement ends without being
#  replaced by another separate license agreement, the license terms below apply
#  from the time at which said agreement ends.
#
#  LICENSE TERMS
#
#  This program is free software: you can redistribute it and/or modify it under the
#  terms of the GNU Affero General Public License, version 3, as published by the
#  Free Software Foundation. This program is distributed in the hope that it will be
#  useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
#  See the GNU Affero General Public License Version 3 for more details.
#
#  You should have received a copy of the GNU Affero General Public license along
#  with this program. If not, see <http://www.gnu.org/licenses/agpl-3.0.en.html>.
#
#####################################################################################

from __future__ import absolute_import

from twisted.trial import unittest

from pytrie import StringTrie


class TestPyTrie(unittest.TestCase):

    def test_empty_tree(self):
        t = StringTrie()
        for key in [u'', u'f', u'foo', u'foobar']:
            with self.assertRaises(KeyError) as e:
                t.longest_prefix_value(key)

    def test_contains(self):
        t = StringTrie()
        test_keys = [u'', u'f', u'foo', u'foobar', u'baz']
        for key in test_keys:
            t[key] = key
        for key in test_keys:
            self.assertTrue(key in t)

    def test_longest_prefix_1(self):
        t = StringTrie()
        test_keys = [u'f', u'foo', u'foobar', u'baz']
        for key in test_keys:
            t[key] = key
        for key in test_keys:
            self.assertEqual(t.longest_prefix_value(key), key)

    def test_longest_prefix_2(self):
        t = StringTrie()
        test_keys = [u'f', u'foo', u'foobar']
        for key in test_keys:
            t[key] = key

        test_keys = {
            u'foobarbaz': u'foobar',
            u'foobaz': u'foo',
            u'fool': u'foo',
            u'foo': u'foo',
            u'fob': u'f',
            u'fo': u'f',
            u'fx': u'f',
            u'f': u'f',
        }
        for key in test_keys:
            self.assertEqual(t.longest_prefix_value(key), test_keys[key])

    def test_longest_prefix_3(self):
        t = StringTrie()
        test_keys = [u'x', u'foo', u'foobar']

        for key in [u'y', u'yfoo', u'fox', u'fooba']:
            with self.assertRaises(KeyError) as e:
                t.longest_prefix_value(key)

    def test_longest_prefix_4(self):
        stored_key = u'x'
        test_key = u'xyz'

        t = StringTrie()
        t[stored_key] = stored_key
        self.assertTrue(stored_key in t)
        self.assertTrue(test_key.startswith(stored_key))
        self.assertEqual(t.longest_prefix_value(test_key), stored_key)

    def test_longest_prefix_5(self):
        self.skip = True
        stored_key = u''
        test_key = u'xyz'

        t = StringTrie()
        t[stored_key] = stored_key
        self.assertTrue(stored_key in t)
        self.assertTrue(test_key.startswith(stored_key))
        self.assertEqual(t.longest_prefix_value(test_key), stored_key)

    test_longest_prefix_5.skip = "pytrie behavior is broken wrt to string keys of zero length!"