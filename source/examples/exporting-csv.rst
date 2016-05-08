Exporting Tabular Data as a CSV
*******************************

Problem
=======

Export data to a CSV file.

Approach
========

Load the data from the databroker into a table (a DataFrame) and use the
pandas package to effeciently export to CSV. Incorporate metadata in the
filename.

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

We'll preface this example by running a scan to generate some example data.
We'll generate three runs, destined for three separate CSV files.

.. ipython:: python

    from bluesky.plans import pchain  # a utility for chaining plans together

    # This plan combines three 'scan' plans.
    # Each scan includes some optional extra metadata that we'll use later.
    master_plan = pchain(scan([det], motor, -10, 10, 15, md={'round': 1}),
                         scan([det], motor, -5, 5, 15, md={'round': 2}),
                         scan([det], motor, -3, 3, 10, md={'round': 3}))
    uids = RE(master_plan)

Here's a simple example that will work for any scan:

.. ipython:: python

    headers = db[uids]
    for h in headers:
        s = h['start']  # the portion of the header with most useful metadata
        table = db.get_table(h)
        filename = '{uid}.csv'.format(**s)
        print('saving table as', filename) 
        table.to_csv(filename)

Using the unique IDs as the filenames ensure we can always go back to find the
original data, but it is not especially easy to navigate through the files.

Here is another example, customized to include our custom metadata field,
'round', in the filename:

.. ipython:: python

    for h in headers:
        s = h['start']  # the portion of the header with most useful metadata
        table = db.get_table(h)
        filename = '{round}_{uid}.csv'.format(**s)
        print('saving table as', filename) 
        table.to_csv(filename)
