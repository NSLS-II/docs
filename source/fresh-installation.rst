Fresh Installation
==================

1. Install mongo 3.x some dedicated server and start the mongo daemon.
2. Conda should be installed by puppet. Add ``/opt/conda/bin`` to the
   ``$PATH``.
3. Install all the data collection software. This can be done in one step
   by install the conda "metapackage" called ``collection``. This package
   includes bluesky, ophyd, pyOlog, and all depedencies. Run this command
   exactly as written:

.. code-block:: bash

    conda create -c nsls2-tag -n collection collection

This means "Install the 'collection' metapackage  from the nsls-tag 'conda
channel' into a new environment also named 'collection'. This creates a
directory at ~/conda_envs/collection, where a new python binary, IPython
binary, and other packages (bluesky, ophyd, numpy, pandas, etc.) are
installed.

To test the new environment, activate it:

.. code-block:: bash

    source activate collection

and check that ``which ipython`` points to a binary under the collection
directory. (To troubleshoot, you might need to refresh bash with the command
``hash -r``.)

4. Create configuration files for metadatastore and filestore. As root user,
   compose two new files:

.. code-block:: bash

    # /etc/metadatastore.yml
    host: hostname
    port: 27017
    database: metadatastore
    timezone: US/Eastern

    # /etc/filestore.yml
    host: hostname
    port: 27017
    database: metadatastore

The metadatastore and filestore Python packages locate this file on import.

5. If this beamline does not yet have an IPython profile for data collection
   under version control, create one.

.. code-block:: bash

    ipython --profile=collection

Now exit IPython. Entering IPython with this command created a directory
structure and some files under ``~/.ipython/profile_collection``. Enter this
directory and put it under version control with the commands:

.. code-block:: bash

    git init
    git add .
    git commmit -m "initial commit"

We focus on the subdirectory that contains Python scripts run by IPython
at startup. From here, look at `beamline configuration <http://nsls-ii.github.io/beamline-configuration.html>`_
documentation. There is some boilerplate startup code that is essential for
using ophyd and bluesky effectively. Then, the rest of the startup scripts
define instances of ophyd objects (motor, detectors, etc.), custom plans
(i.e., scans), and any user convenience functions.
