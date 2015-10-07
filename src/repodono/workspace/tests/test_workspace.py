# -*- coding: utf-8 -*-
from plone.app.testing import TEST_USER_ID
from zope.component import queryUtility
from zope.component import createObject
from plone.app.testing import setRoles
from plone.dexterity.interfaces import IDexterityFTI
from plone import api

from repodono.workspace.testing import REPODONO_WORKSPACE_INTEGRATION_TESTING  # noqa
from repodono.workspace.interfaces import IWorkspace

import unittest


class WorkspaceIntegrationTest(unittest.TestCase):

    layer = REPODONO_WORKSPACE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='Workspace')
        schema = fti.lookupSchema()
        self.assertEqual(IWorkspace, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='Workspace')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='Workspace')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IWorkspace.providedBy(obj))

    def test_adding(self):
        self.portal.invokeFactory('Workspace', 'Workspace')
        self.assertTrue(
            IWorkspace.providedBy(self.portal['Workspace'])
        )
