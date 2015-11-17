repodono.workspace
==================

This is an implementation of a framework that enables the embedding
external data into a Plone instance, where the data is tracked in a
proper version control system (such as Git or Mercurial).  This can
source code from external repositories.

This is akin to a standalone implementation of what was provided by
pmr2.app.workspace.

.. image:: https://travis-ci.org/repodono/repodono.workspace.svg?branch=master
  :target: https://travis-ci.org/repodono/repodono.workspace
.. image:: https://coveralls.io/repos/repodono/repodono.workspace/badge.svg?branch=master&service=github
  :target: https://coveralls.io/github/repodono/repodono.workspace?branch=master

Features
--------

- Foundation for a generic dexterity type that allows embedding of code
  resources into Plone.
- Specific formats are determined by extensions.  By default a git and
  mercurial implementation are provided (as separate packages).

Documentation
-------------

Full documentation for end users can be found in the "docs".


Installation
------------

Install repodono.workspace by adding it to your buildout::

   [buildout]

    ...

    eggs =
        repodono.workspace


and then running "bin/buildout"

Contribute
----------

- Issue Tracker: https://github.com/repodono/repodono.workspace/issues
- Source Code: https://github.com/repodono/repodono.workspace


License
-------

The project is licensed under the GPLv2.
