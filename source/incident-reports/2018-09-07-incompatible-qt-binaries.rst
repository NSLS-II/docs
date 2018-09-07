2018-08-07 Incompatible Qt Binaries
***********************************

Summary
=======

In a the first trial deployment of a new environment at LIX,
``from PyQt5 import QtCore`` segfaulted.  There was a qt binary from
conda-forge in the ``nsls2-tag`` channel. It is binary incompatible with the
pyqt from the ``anaconda`` channel. Having picked that version of qt pinned a
bunch of other compiled dependencies, we can not install any other version of
qt. The offending files have been removed (we think from both) alexandria and
pergamon, as well as some other files that were copied from CF. We
re-generated the enviroment yml files (but not the metapackages) and redeployed
to LIX and TES, the only two beamlines we deployed to.


Timeline
========

Lessons Learned
===============

What went well
--------------

#. Our acceptance test process led us to catch the problem before we walked
   away from the beamline.
#. We tested at LIX and TES before a wide rollout.

What went wrong
---------------

#. We didn't have clarity that conda-forge binaries containing any native
   extensions should not be copied into ``nsls2-tag``.

Where we got lucky
------------------

Action items
============

These are only sample subheadings. Every action item should have a GitHub issue
(even a small skeleton of one) attached to it, so these do not get forgotten.

Process improvements
--------------------

1. {{ summary }} [link to github issue]
2. {{ summary }} [link to github issue]

Documentation improvements
--------------------------

1. {{ summary }} [link to github issue]
2. {{ summary }} [link to github issue]

Technical improvements
----------------------

1. {{ summary }} [link to github issue]
2. {{ summary }} [link to github issue]
