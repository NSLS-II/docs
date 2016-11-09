Tutorials
=========

About
-----

Before You Go
+++++++++++++

Bring a laptop. These tutorials are interactive.

If you want to try the software on your personal laptop (which we encourage!)
follow the instructions on `this page <https://github.com/NSLS-II/tutorial>`_.
If you have difficulty with the installation, email a member of the DAMA group
or attend office hours (see below).

Alternatively, you can use our "sandbox" environment at
`https://try.nsls2.bnl.gov <https://try.nsls2.bnl.gov>`_ to experiment with
the software without installing anything. (Be aware that all work you do this
is emphemeral; it is automatically deleted after some period of inactivity.)
(Formerly, this was only available inside the VPN. Now it is fully public to
the outside world.)

Schedule
--------

Office Hours
++++++++++++

Office hours are every Friday 1-3 in Room 156 of Building 741. 

Current Sessions
++++++++++++++++

Tutorials are normally presented twice: first on a Wednesday, and then a repeat
the following Tuesday.

* 10/26 and 11/1: :ref:`conda-ipython`
* 11/2 and 11/8: :ref:`daq1`
* 11/9 and 11/15: :ref:`broker`
* 11/16 and 11/22: :ref:`daq2`
* 11/23 and 11/29: :ref:`daq3`
* 11/30 and 12/6: :ref:`daq4`

Past Sessions
+++++++++++++

* 9/7 and 9/13: :ref:`advanced-git`
* 8/31 and 9/6: :ref:`basic-git`
* 8/17 and 8/23: Bluesky Plans (This material has been reworked and expanded into
  Data Acquition I and II.)
* 8/16 :ref:`conda-ipython`
* 9/14 and 9/20: :ref:`broker`
* 9/21 and 9/27: :ref:`daq1`
* 9/28 and 10/4: :ref:`amostra`
* 10/5 and 10/11: :ref:`daq2`
* 10/12 and 10/18: :ref:`daq3`
* 10/19 and 10/25: :ref:`daq4`


.. _conda-ipython:

Conda & IPython
---------------

Goals
+++++

* Install conda and IPython.
* Learn how to install different versions of the same software (e.g. a "stable"
  version and an "experimental" version) on the same computer.
* Get familiar with IPython, the interactive interpreter for scientific Python.
* Learn many practical IPython features.

Resources
+++++++++

* `Download & Install miniconda <http://conda.pydata.org/miniconda.html>`_
* `IPython cheatcheat <_static/ipython-cheatsheet-v1.pdf>`_

.. _basic-git:

Basic Git
---------

Goals
+++++

* Install git.
* Create a GitHub account.
* Make a directory of text files and use git for version control.
* Upload changes to GitHub.

Resources
+++++++++

* `Software Carpentry git tutorial <https://swcarpentry.github.io/git-novice/>`_
* `Repository of tutorial materials <https://github.com/NSLS-II/git-tutorial>`_ 

.. _advanced-git:

Git and GitHub for Collaborative Development
--------------------------------------------

Goals
+++++

* On GitHub, create a "fork" of a community-run git repository.
* Submit a "pull request" to share changes with the community.
* Understand and practice the "git flow" workflow for managing collaboration.

Resources
+++++++++

* `Install git <https://help.github.com/articles/set-up-git/>`_
* `Git Flow <https://guides.github.com/introduction/flow/>`_
* `The Git Parable <http://tom.preston-werner.com/2009/05/19/the-git-parable.html>`_
* `DAMA Development Guide <https://scikit-beam.github.io/scikit-beam/resource/dev_guide/index.html#development-guide>`_

.. _broker:

Data Broker: Searching and Loading Data
---------------------------------------

Goals
+++++

* Search for data based on proposal number, experiment type, etc.
* Enter metadata into a scan and using it find that scan in a search.
* Retrieve tabular data and export it as CSV file.
* Retrieve image data and plot it.

Resources
+++++++++

* `tutorial materials <https://github.com/NSLS-II/broker-tutorial>`_
* `databroker documentation <https://nsls-ii.github.io/databroker>`_

.. _daq1:

Data Acquisition I: Bluesky Basics
----------------------------------

This tutorials will cover the first three sections of the
`bluesky documentation <https://nsls-ii.github.io/bluesky>`_.

Goals
+++++

* Understand the key concepts: RunEngine, plan, and document.
* Write some very basic custom plans (what SPEC users call "macros")
* Understand how to specify custom metadata.

Resources
+++++++++

* `bluesky documentation <https://nsls-ii.github.io/bluesky>`_

.. _amostra:

Amostra: Management of Sample Metadata in Python
------------------------------------------------

Goals
+++++

TBD

Resources
+++++++++

* `amostra documentation <https://nsls-ii.github.io/amostra>`_

.. _daq2:

Data Acquisition II: Survey of "Plans"
--------------------------------------

This tutorials starts with the
`*Plans* section bluesky documentation <https://nsls-ii.github.io/bluesky/plans.html>`_,
focusing on the first section ("Pre-assmebled Plans").

Goals
+++++

* Survey bluesky's built-in plans for simple scans, multi-motor coordination,
  and more.

Resources
+++++++++

* `bluesky documentation <https://nsls-ii.github.io/bluesky>`_

.. _daq3:

Data Acquisition III: Basic Custom "Plans"
------------------------------------------

This tutorial continues where II left off, walking through the
`*Plans* section bluesky documentation <https://nsls-ii.github.io/bluesky/plans.html>`_,
focusing on "Stub Plans" and the examples following them.

Goals
+++++

* Learn intermediate techniques for writing custom plans and scripts.

.. _daq4:

Data Acquisition IV: Advanced Custom "Plans"
--------------------------------------------

This tutorial continues where III left off, walking through the
`*Plans* section bluesky documentation <https://nsls-ii.github.io/bluesky/plans.html>`_,
focusing on "Plan Preprocessors" and the examples following them.

Goals
+++++

* Learn about advanced plan customization using preprocessors.

Resources
+++++++++

* `bluesky documentation <https://nsls-ii.github.io/bluesky/plans.html>`_
