# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s repodono.workspace -t test_workspace.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src repodono.workspace.testing.REPODONO_WORKSPACE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_workspace.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Workspace
  Given a logged-in site administrator
    and an add workspace form
   When I type 'My Workspace' into the title field
    and I submit the form
   Then a workspace with the title 'My Workspace' has been created

Scenario: As a site administrator I can view a Workspace
  Given a logged-in site administrator
    and a workspace 'My Workspace'
   When I go to the workspace view
   Then I can see the workspace title 'My Workspace'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add workspace form
  Go To  ${PLONE_URL}/++add++Workspace

a workspace 'My Workspace'
  Create content  type=Workspace  id=my-workspace  title=My Workspace


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the workspace view
  Go To  ${PLONE_URL}/my-workspace
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a workspace with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the workspace title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
