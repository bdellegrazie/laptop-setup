#!/usr/bin/env python

# key_startswith filter - group_by a prefix for group_var variables
#
#    * Enables creating a collection (list) from disparate sets of group_var
#      variables linked by a common prefix.
#
#    e.g.:
#
#    in
#    group_vars/all/test.yml:
#      test__default: [ "a", "b" ]
#      test_list: "{{ hostvars[inventory_hostname] | key_startswith('test__') |
#        flatten | list }}"
#
#    group_vars/somehost/test.yml
#      test__somehost: [ "c", "d" ]
#
#    When executing on "somehost" this results in:
#    test_list: ["a","b","c","d"]
#    * order is not determinate *


# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import unittest

from jinja2 import Undefined


def filter_dict_keystartswith(d, prefix):
    """
    Each key of ``d`` is compared prefix wise with ``prefix``.
    If match, return value of ``d[k]`` as list

    Args:
        d: Dictionary of Dictionaries
        prefix: prefix to match keys in ``d`` against.

    Returns:
        List of values of ``d`` with key prefix ``prefix``

    """
    if d is None or isinstance(d, Undefined):
        return d
    return [v for k, v in d.items() if k.startswith(prefix)]


class FilterModule(object):
    def filters(self):
        return {
            'key_startswith': filter_dict_keystartswith,
        }


class TestFilterKeyStartsWith(unittest.TestCase):
    def test_source_empty(self):
        d = {}
        self.assertListEqual(filter_dict_keystartswith(d, 'notaprefix'), [])

    def test_prefix_missing(self):
        d = {'prefix_extra': 1}
        self.assertListEqual(filter_dict_keystartswith(d, 'notaprefix'), [])

    def test_prefix_match(self):
        d = {'prefix_extra': 1, 'prefix_other': 2}
        self.assertListEqual(filter_dict_keystartswith(d, 'prefix_'), [1, 2])


if __name__ == '__main__':
    unittest.main()
