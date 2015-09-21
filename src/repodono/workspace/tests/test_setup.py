# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from repodono.workspace.testing import REPODONO_WORKSPACE_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that repodono.workspace is properly installed."""

    layer = REPODONO_WORKSPACE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if repodono.workspace is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('repodono.workspace'))

    def test_browserlayer(self):
        """Test that IRepodonoWorkspaceLayer is registered."""
        from repodono.workspace.interfaces import IRepodonoWorkspaceLayer
        from plone.browserlayer import utils
        self.assertIn(IRepodonoWorkspaceLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = REPODONO_WORKSPACE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['repodono.workspace'])

    def test_product_uninstalled(self):
        """Test if repodono.workspace is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('repodono.workspace'))

    def test_browserlayer_removed(self):
        """Test that IRepodonoWorkspaceLayer is removed."""
        from repodono.workspace.interfaces import IRepodonoWorkspaceLayer
        from plone.browserlayer import utils
        self.assertNotIn(IRepodonoWorkspaceLayer, utils.registered_layers())
