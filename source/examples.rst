Examples
********

These examples assume:

1. The user has followed the Data Collection Quickstart or Data Analysis
   Quickstart. (See links on menu at left.)
2. The user has an IPython profile where they can define instances of motors
   and detectors and stash other useful snippets of code. Typically,
   this is located at ``~/.ipython/profile_collection/startup/``. (For
   more, see Deployment Details > Beamline Configuration on the menu at left.)
3. In the user's IPython profile, an instance of the RunEngine has already
   been defined and, if desired, configured to save data. To experiment
   without saving data, make an instance of the RunEngine like so:

   .. ipython:: python

       from bluesky import RunEngine
       RE = RunEngine({})

.. toctree::
    :maxdepth: 1

    examples/simple-scan
    examples/count-with-exp-decay-delay
    examples/flyer-progress-bar
