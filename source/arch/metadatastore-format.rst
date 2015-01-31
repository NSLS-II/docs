*******************************
Format of Metadatastore Entries
*******************************

Introduction
============

The metadatastore is based on the concept of documents which are either
events, or descriptions of events.  An ``event`` is a quantum of data
stored in the metadata store and represents an *action* at a given time. For
example: "*measurement of 8 scaler chanels*", "*trigger detectors*" or
"*start run*".

Expanding the notion of **events**, these can also be used for derived data.
For example, an event could be the result of a data analysis or reduction
routine which was run at a certain time.

The document schemas in this document are written using ``jsonschema``.  The
full spec http://json-schema.org/ is basically un-readable.  A more readable
introduction https://spacetelescope.github.io/understanding-json-schema/index.html.


.. todo::
    Expand this section




Time
====

One of the cornerstones of this data acquisition and analysis method is the use
of *time* as the method by which data can be aligned and correlated. A single
``event`` should have happened at a certain quantum of time with the
determination of what a time *quantum* is left to the details of the
experiment. Time however, can be horrendously messy. Throughout this
section we use two terms, ``timestamp`` and ``time``. These mean


time
    The date/time as found by the client when an ``event`` is
    created.  This could be a date-time format as determined by the underlying
    storage method (for example a database).

timestamp
   A (usually *float*) representation of the hardware time when a
   certain value was obtained. Wherever possible this should be read from
   hardware. For example, this could be the *EPICS* timestamp from when the
   record processed which provides the value.


We use the literal ``<time>`` to indicate a client side date/time and
``<timestamp>`` to represent the numerical timestamp.

.. todo::
    Add dictionary of reserved keys such as ``timestamp``, ``id``
    Expand for data collection, using event model


Documents
=========

.. graphviz:: document_overview.dot

Events
------

Events are the smallest quantum of data stored in the metadatastore. They group
values which are associated with temporally bundled data. The definition of
"temporally identical" is determined by the DAQ system. For example, the 32
channels in a scaler can be considered to be temporally identical because they
are hardware synchronized. Inclusion of a CCD image (with a reference to the
file store) can be included if this event is triggered at the same time, either
by software or hardware.  Each ``event`` contains the data values and a client
side timestamp of when the even was created. The same logic is applied to
``trigger events``. These are grouped with temporally identical triggers (again
determined by the DAQ philosophy).


Event Descriptor Document
~~~~~~~~~~~~~~~~~~~~~~~~~

Schema
++++++

The field ``seq_num`` is used to order the events in the order in which they were
created.

``event_descriptor`` ``keys`` take the form::

   'key_name': {"source": "NAMESPACE:NAME", "external": "NAMESPACE:NAME"}

    Description of the key_name dictionary:

    source
        - The reference to the physical piece of hardware that produced this data

        NAMESPACE
            Things like ``PV``. Unclear what other options might be.
        NAME
            If NAMESPACE is ``PV`` then this should be the PV. Otherwise,
            something that makes sense to the user

    external, optional
        - The reference to the location where the data is being stored.
          - If this key is not present, then the data is stored inside the data
            field of the corresponding ``Event`` document.
          - If this key is present, then the ``value`` field of the ``data``
            dictionary inside the ``Event`` document is interpreted as a unique
            key that can be used to retrieve corresponding data from the
            service described by the value of the ``external`` key

        NAMESPACE
            Things like ``FILESTORE``. Unclear what other options might be.
        NAME, optional
            Used to provide any additional information required to retrieve
            data that ``NAMESPACE`` does not provide. Really unclear what might
            go here.



Example
+++++++

Event descriptors are used to describe an array of events which can form an
event stream of a collection of events. For example a run forms
event_descriptors at run start to define the data collected. For the example
above ``event`` is described by the ``event_descriptor``::

    {
        "uid": <unique_id>,
        "keys": {
            "chan1": {"source": "PV:XF:23ID1-ES{Sclr:1}.S1"},
            "chan2": {"source": "PV:XF:23ID1-ES{Sclr:1}.S2"},
            "chan3": {"source": "PV:XF:23ID1-ES{Sclr:1}.S3"},
            "chan4": {"source": "PV:XF:23ID1-ES{Sclr:1}.S4"},
            "chan5": {"source": "PV:XF:23ID1-ES{Sclr:1}.S5"},
            "chan6": {"source": "PV:XF:23ID1-ES{Sclr:1}.S6"},
            "chan7": {"source": "PV:XF:23ID1-ES{Sclr:1}.S7"},
            "chan8": {"source": "PV:XF:23ID1-ES{Sclr:1}.S8"},
            "pimte": {"source": "CCD:name_of_detector", "external": "FILESTORE"}
        },
        "begin_run_event": <unique_id>,
        "time": <time>,
    }



Event Documents
~~~~~~~~~~~~~~~


Schema
++++++

Example
+++++++

Measure events contain the data measured at a certain instance in time or
explicit point in a sequence. For example::

    {
        "uid": <unique_id>,
        "seq_num": <integer>,
        "ev_desc": <unique_id>,
        "data": {
            "chan1": {"value": <value>, "timestamp": <ts>},
            "chan2": {"value": <value>, "timestamp": <ts>},
            "chan3": {"value": <value>, "timestamp": <ts>},
            "chan4": {"value": <value>, "timestamp": <ts>},
            "chan5": {"value": <value>, "timestamp": <ts>},
            "chan6": {"value": <value>, "timestamp": <ts>},
            "chan7": {"value": <value>, "timestamp": <ts>},
            "chan8": {"value": <value>, "timestamp": <ts>},
            "pimte": {"value": <unique_id>, "timestamp": <ts>}
        },
        "time": <time>,
    }

Where the keys ``uid``, ``ev_desc``, ``time`` and ``timestamp`` refer to
the unique id, a link to the event descriptor the time and the EPICS timestamp
respectively.


Start Run Events
----------------


Schema
++++++

Example
+++++++

The beginning of a data collection run creates an event which contains
sufficient metadata and information to describe the data collection. For
example, this is where beamline config information is located. The start run
event also serves as a searchable entity which links all data associated by an
event. For example::

    {
        "uid": <unique_id>,
        "scan_id": <non-unique-id>, # anything sortable
        "beamline_id:: <string>,
        "sample": {
            "uid": <unique_id>
            "id": <number>,
            "description": <string>
        }
        "project": <string>,
        "beamline_config": {
            "diffractometer": {
                "geometry": <string>,
                "xtal_lattice": {
                    "a": <float>,
                    "b": <float>,
                    "c": <float>,
                    "alpha": <float>,
                    "beta": <float>,
                    "gamma": <float>
                }
                "UB": [...]
            }
        },
        "time": <time>
    }



End Run Events
--------------

Schema
++++++

Example
+++++++


With the corresponding end run event as::

    {
        "uid": <id>,
        "begin_run_event": <id>,
        "reason": <string>,
        "time": <time>,
        "start_id": <unique_id>
    }

The field ``reason`` can be used to describe why a run ended e.g. was it aborted or
was there an exception during data collection. The field ``start_id`` is a
pointer to the start event.
