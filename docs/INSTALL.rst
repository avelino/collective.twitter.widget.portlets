Install
-------

 * When you're reading this you have probably already run
   ``easy_install collective.twitter.widget.portlets``. Find out how to install setuptools
   (and EasyInstall) here:
   http://peak.telecommunity.com/DevCenter/EasyInstall

 * Create a file called ``collective.twitter.widget.portlets-configure.zcml`` in the
   ``/path/to/instance/etc/package-includes`` directory.  The file
   should only contain this::

       <include package="collective.twitter.widget.portlets" />

Alternatively, if you are using zc.buildout and the plone.recipe.zope2instance
recipe to manage your project, you can do this:

 * Add ``collective.twitter.widget.portlets`` to the list of eggs to install, e.g.:

    [buildout]
    ...
    eggs =
        ...
        collective.twitter.widget.portlets

  * Re-run buildout, e.g. with:

    $ ./bin/buildout

You can skip the ZCML slug if you are going to explicitly include the package
from another package's configure.zcml file.
