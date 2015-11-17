# -*- coding: utf-8 -*-
from plone.testing import layered
import doctest
import unittest
from repodono.workspace.testing import \
    REPODONO_WORKSPACE_DUMMY_STORAGE_FUNCTIONAL_TESTING


tests = (
    'storage.txt',
)


def test_suite():
    return unittest.TestSuite(
        [layered(doctest.DocFileSuite(f, optionflags=doctest.ELLIPSIS),
                 layer=REPODONO_WORKSPACE_DUMMY_STORAGE_FUNCTIONAL_TESTING)
            for f in tests]
    )
