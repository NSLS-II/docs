***********************************************
Updating Metapackages and Building Environments
***********************************************

Background
==========

A `metapackage <https://conda.io/docs/glossary.html#metapackage>`_
is a conda package that contains only a list of dependencies but not functional
code itself.

We maintain several metapackages:

* ``analysis``, which depends on libraries for data analysis (e.g.
  scikit-beam), data acess (e.g. databroker) and simulation (e.g. bluesky)
* ``collection``, which depends on ``analysis``, so it includes a superset of
  those dependencies, adding some additional ones only needed for data
  acquisition (e.g. nslsii)
* several beamline-specific packages, with names like ``11-id-chx-analysis`` or
  ``11-id-chx-collection`` that depend on the general ``analysis`` or
  ``collection`` package and add some beamline-specific requirements

They are located in the ``recipes-tag`` directory of
`NSLS-II/lightsource2-recipes <https://github.com/NSLS-II/lightsource2-recipes>`_.

Publishing a New Metapackage
============================

Select packages are pinned to ensure that conda resolves the right version.
Update these pins, and add any new dependencies.

Finally, when you are ready to
publish the new metapackages, submit a PR that bumps the version numbers in the
recipes. The metapackages have the versioning scheme
``{{ year }}C{{ cycle }}.{{ version }}``, such as ``2018C3.0``.
The ``{{ version }}`` is used for mid-cycle patch releases.

As with :doc:`software releases <releasing-software>`, the builder
will detect the change and make the new metapackage available on the conda
server.

Revoking a Bad Metapackage
--------------------------

We often discover a mistake in a metapackage shortly after publishing it. If
the metapackage has already been deployed to beamlines, it should not be
deleted; instead a new version should be released. But if we catch the error
early, during deployment, we remove the bad metapackage and re-publish under
the same version.

#. Delete the package from the public conda channel. Visit
   https://anaconda.org/lightsource2-tag/analysis/files and/or
   https://anaconda.org/lightsource2-tag/collection/files. Log in. Delete the
   offending files.
#. Delete the package from the internal conda channel. On any server inside
   the Controls network that has conda installed (e.g. xf23id1-srv1) run:

   .. code-block:: bash

      /opt/conda/bin/anaconda remove nsls2-tag/collection=XXX
      /opt/conda/bin/anaconda remove nsls2-tag/collection=XXX

   where ``XXX`` is a version like ``2018C3.0``.

The order is important because the "mirroring" agent that copies packages from
the public conda channel to the internal one can undo your work! To avoid this,
we deleted the external/public copy first.

Publishing a New Environment File
=================================

An environment is similar to a metapacakge, but more strictly specified. It
contains the recursive set of every dependency, along with the exact version
and build and which channel the package was obtained from. This is what we use
to deploy at beamlines.

Log into any server inside the Controls network that has conda installed
(e.g. xf23id1-srv1).
