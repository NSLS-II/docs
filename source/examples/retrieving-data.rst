Retrieving metadata, tabular data, and image data
*************************************************

Problem
=======

Retrieve metadata, tabular data, or image data for analysis, processing, or
export.

Approach
========

Use the databroker, the all-in-one interface to saved data.

Search for the *header(s)* of the run(s) of interest. Explore the "raw"
interface, which provides maximum flexiblity and performance. Then use
some "convenience functions" for loading a table or a stack of images.

Example Solution
================

First, serach for the *header(s)* of the run(s) of interest. (The headers
contain metadata. See :doc:`/examples/header-contents` for details.)

.. ipython:: pyton
    :suppress:

    from bluesky.scans import scan
    from bluesky import RunEngine
    # generate fake data


.. ipython:: python

    db.get_table(h)

    db.get_images(h, 'img')
