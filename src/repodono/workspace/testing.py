# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import repodono.workspace


class RepodonoWorkspaceLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=repodono.workspace)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'repodono.workspace:default')


REPODONO_WORKSPACE_FIXTURE = RepodonoWorkspaceLayer()


REPODONO_WORKSPACE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(REPODONO_WORKSPACE_FIXTURE,),
    name='RepodonoWorkspaceLayer:IntegrationTesting'
)


REPODONO_WORKSPACE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(REPODONO_WORKSPACE_FIXTURE,),
    name='RepodonoWorkspaceLayer:FunctionalTesting'
)


REPODONO_WORKSPACE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        REPODONO_WORKSPACE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='RepodonoWorkspaceLayer:AcceptanceTesting'
)
