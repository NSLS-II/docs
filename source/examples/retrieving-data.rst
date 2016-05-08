Retrieving metadata, tabular data, and image data
*************************************************

Problem
=======

Retrieve metadata, tabular data, or image data for analysis, processing, or
export.

Approach
========

Use the databroker, the all-in-one interface to saved data.

Retrieve the metadata for the run(s) of interest. Retrieve the data itself
in three different modes:

* a general-purpose method, which provides maximum flexiblity and performance
* a convenient method for retrieving tabular data
* a convenient method for retrieving image data

Example Solution
================

.. ipython:: python
    :suppress:

    from bluesky import RunEngine
    from bluesky.plans import scan
    from bluesky.examples import motor, det
    import metadatastore.commands as mds
    # import filestore.api as fs
    # from databroker import Broker
    # db = Broker(mds, fs)
    from databroker import db
    RE = RunEngine({})
    RE.subscribe_lossless('all', mds.insert)

We'll preface this example by generating some example data.

.. ipython:: python

    uid, = RE(scan([det], motor, -10, 10, 15))

The unique id of the data set has been stashed in the variable ``uid``. We can
use that to retrieve the data from the databroker.

.. ipython:: python

    h = db[uid]

What we get back is a *header*, which contains all of the metadata from the
run.  For example, we can review the names of the detector(s) involved:

.. ipython:: python

    h['start']['detectors']

There is a lot of information in ``h``. See :doc:`/examples/header-contents`.
What about the data itself?

General-Purpose Method
----------------------

.. ipython:: python

    events = db.get_events(h)

In the variable ``events``, we now have a collection of documents
(dictionary-like mappings of names to values). Each event corresponds to 
a single data point, a row in table.

For performance reasons, the data has not actually been loaded yet. The data
is loaded one point at a time if loop through ``events``. (This is very
useful for applications where we don't need to load the entire data set.)

To load the entire data set once, convert ``events`` to a list.

.. ipython:: python

    events = list(events)  # for large data sets, this takes awhile

Let's look at all the data in the events.

.. ipython:: python

    [event['data'] for event in events]

You might be thinking, "Just give me data!" As promised, the general-purpose
method is flexible, but it lacks terseness. For more direct methods, read on!

To learn more about the structure of an ``event``, refer to the
`overview of the document model <nsls-ii.github.io/architecture-overview.html>`_.

Retrieving a Table
------------------

.. ipython:: python

    db.get_table(h)

The result is a DataFrame. One can access individual columns like so:

.. ipython:: python

    table = db.get_table(h)
    table['det']

perform fast array computations using numpy

.. ipython:: python

    import numpy as np

    np.mean(table)

and much, much more.

.. note::

    The variable ``table`` here is a pandas DataFrame, scientific Python's
    answer to the spreadsheet. Read the
    `pandas documentation <http://pandas.pydata.org/pandas-docs/stable/>`_
    for more. It's an extremely powerful package for analyzing tabular
    data.

Narrowing the Results
+++++++++++++++++++++

The ``get_table`` method accepts several optional arguments which can be used
to filter the results (and corespondingly speed up the retrieval). Examples:

.. ipython:: python

    db.get_table(h, ['det'])  # just include the 'det' column

Retrieving Images
-----------------

.. warning::

    The short answer is, ``db.get_table(h, 'image_field_name')``. This section
    is to be written.
