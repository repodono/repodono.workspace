# -*- coding: utf-8 -*-


def post_install(context):
    """Post install script"""
    if context.readDataFile('repodonoworkspace_default.txt') is None:
        return
    # Do something during the installation of this package


def uninstall(context):
    """Uninstall script"""
    if context.readDataFile('repodonoworkspace_uninstall.txt') is None:
        return
    # Do something during the uninstallation of this package
