.. NSLS-II arch documentation master file, created by
   sphinx-quickstart on Sun Jan 18 10:00:09 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

NSLS-II Software Documentation
******************************

We are deploying an event-based data collection and analysis framework.

.. image:: _static/collection-overview.gif
   :align: center

Design Goals
============

* Provide an integrated, **end-to-end solution** for data collection and analysis.
* Support **streaming** data processing, variously called "in-line" or "live."
* Use **existing, open-source technologies and languages**; avoid inventing a
  domain-specific language.
* Leverage tools from the rapidly-growing **scientfic Python** community.
* Adhere to good modern software practices, especially code review and
  automated testing, with the goal of enabling **large-scale collaboration**
  while maintaining **stability and robustness**.
* Establish **clear, consistent interfaces** (meaning inputs and outputs, not
  graphical interfaces) that allow project components to be used independently,
  extended, and interfaced with other, outside projects.

Software Packages
=================

The following software packages work together to handle different aspects of
data collection and analysis. They interoperate by sharing a common
:ref:`event-based model <architecture>`. Each package has its own detailed
documentation, linked below.

* Data Collection Packages
    * `bluesky <http://nsls-ii.github.io/bluesky>`_ -- a framework for specifying and executing experiments
    * `ophyd <http://nsls-ii.github.io/ophyd>`_ -- a collection of Python objects that represent hardware, providing a common high-level interface
* Data Access Packages
    * High-level Data Access
        * `databroker <http://nsls-ii.github.io/databroker>`_ -- a simple interface that pulls together data from all sources
    * Low-Level Data Storage and Access
        * metadataclient (preferred), metadatastore (deprecated)
        * filestore
* Data Munging Packages
    * `datamuxer <http://nsls-ii.github.io/datamuxer>`_ -- a "de-multiplexer" for alignment and basic processing of asynchronous, event-based data
* Data Export Packages
    * `suitcase <http://nsls-ii.github.io/suitcase>`_ -- a simple proof-of-concept, exporting experiment data and metadata from a database to a stand-alone file
* Scientific Data Processing Packages
    * the built-in subscriptions in `bluesky <http://nsls-ii.github.io/bluesky>`_
    * Beamline-specific \*tools repositories:
        * `csxtools <https://nsls-ii-csx.github.io/csxtools/>`_
        * `chxtools <https://github.com/NSLS-II-CHX/chxtools>`_ (undocumented)
        * `hxntools <https://github.com/NSLS-II-CHX/hxntools>`_ (undocumented)
        * `xpdtools <https://github.com/NSLS-II-XPD/xpdtools>`_ (placeholder)

.. toctree::
   :hidden:
   :maxdepth: 2

   architecture-overview
   collection-quick-start
   analysis-quick-start
   sandbox
   deployment-details
   resources
   technologies

.. toctree::
   :hidden:
   :caption: Data Collection

   bluesky <https://nsls-ii.github.io/bluesky>
   ophyd <https://nsls-ii.github.io/ophyd>

.. toctree::
   :hidden:
   :caption: Data Access

   databroker <https://nsls-ii.github.io/databroker>

.. toctree::
   :hidden:
   :caption: Data Munging

   datamuxer <https://nsls-ii.github.io/datamuxer>

.. toctree::
   :hidden:
   :caption: Data Export

   suitcase <https://nsls-ii.github.io/suitcase>

.. toctree::
   :hidden:
   :caption: GitHub Links

   NSLS-II repositories <https://github.com/NSLS-II/>
   Wish List <https://github.com/NSLS-II/wishlist/issues>
   Bug Reports <https://github.com/NSLS-II/Bug-Reports/issues>
