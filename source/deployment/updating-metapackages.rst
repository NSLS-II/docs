***********************************************
Updating Metapackages and Building Environments
***********************************************

See :doc:`../conda` for background on the function and location of the
components.

Overview
========

1. Update the dependencies in the metapackages.
2. Publish the metapackages.
3. Create an environment file from the metapackage.

Metapackages
============

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
#. Delete the package from the internal conda channel: ssh to ``alexandria``
   (which is inside the Controls network) and run:

   .. code-block:: bash

      sudo rm -f /www/conda/nsls2-tag/linux-64/analysis-XXX-0.tar.bz2
      sudo rm -f /www/conda/nsls2-tag/linux-64/collection-XXX-0.tar.bz2

   where ``XXX`` is a version like ``2018C3.0``.

The order is important because the "mirroring" agent that copies packages from
the public conda channel to the internal one can undo your work! To avoid this,
we deleted the external/public copy first.

Publishing a New Environment File
=================================

Log in to any server on the Controls network that has conda installed (e.g
xf23id1-srv1)
