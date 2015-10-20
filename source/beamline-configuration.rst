.. highlight:: bash
**********************
Beamline Configuration
**********************

IPython profiles
----------------

Configuration can be done interactively or in a Python script.
At NSLS-II, configuration is done by startup scripts that are part of an
`IPython profile <https://ipython.org/ipython-doc/dev/config/intro.html#profiles>`_
. But note that it is not essential to use IPython or IPython profile in 
general -- this is just a convenience.

At the time of this writing, all profiles are stored in or at least soft-linked
from ``~/.ipython`` in the user profile of the beamline account (e.g.,
``xf11id``). In the future, we want users to perform data collection under
their own user accounts, and we will probably move the profiles to a system
location like ``/usr/share/ipython``.

The standard profile is called "collection," and the startup scripts are
located in ``~/.ipython/profile_collection/startup/``. As stated in the on
quick start page, they can be invoked by typing:

.. code-block:: bash

    ipython --profile=collection

Boilerplate configuration
-------------------------

Some boilerplate setup is done in the module ``bluesky.standard_config``. It
does the following things:

#. Set up an instance of the RunEngine in the "global state" varible, ``gs``.

#. Fill in some required metadata, ``owner`` and ``group`` using the current
   UNIX username and a group.

#. To make metadata persistent across sessions (e.g., incrementing the
   user-friendly scan ID) look for a "history" file in a list of standard
   locations. If one is not found, try to create one.

#. Subscribe metadatastore insersion functions to the stream of Documents.
   Make it a "critical subscription," meaning that it gets a lossless stream
   of Events and that if an exception is raised, the scan is stopped.
   (Normal user subscriptions get a potentially lossy stream, for performance,
   and any excpetions raised in subscriptions are ignored by default so as not
   to interrupt the data collection.)

#. Define convenience functions. The most important one is ``olog_wrapper``,
   which can be used later in the configuration process to hook up Olog to
   the RunEngine's logbook output.

#. It imports the "SPEC-like" simple scan API, some commonly-used callbacks,
   the databroker API functions, and a couple others.


Example Configuration File
--------------------------

This is a example startup file.::

    from bluesky.standard_config import *  # get all of the above for free

    gs.RE.md['beamline_id'] = 'YOUR_BEAMLINE_HERE'
    # For now, this is required, but it is going away soon:
    gs.RE.md['config'] = {}

    from ophyd.commands import *  # imports mov, wh_pos, etc.

    # Import matplotlib and put it in interactive mode.
    import matplotlib.pyplot as plt
    plt.ion()

    # Make ophyd less verbose.
    # (Do not spew DEBUG messages each time a device connects.)
    import logging
    from ophyd.session import get_session_manager
    sessionmgr = get_session_manager()
    sessionmgr._logger.setLevel(logging.INFO)

Configuring the Olog
--------------------

This piece actually requires IPython. In the profile directory, such as
``~/.ipython/profile_collection``, edit the file ``ipython_config.py``.

Add the line::::

    c.InteractiveShellApp.extensions = ['pyOlog.cli.ipy']

Back in a startup file, add:::

    # Set up the logbook.
    sessionmgr['olog_client'] = olog_client
    gs.RE.logbook = olog_wrapper(olog_client, ['Data Acquisition'])

Defining Hardware Objects
-------------------------

TODO

Set up Default ("Global State")
-------------------------------

Set attributes of ``gs``. This can be done interactively or in a startup file.::

    gs.DETS = [det1, det2]
    gs.TABLE_COLS = ['det1']
    gs.PLOT_Y = 'det1'

