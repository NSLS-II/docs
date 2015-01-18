Format of metadatastore entries
===============================

Document types
--------------

The metadatastore is based on the concept of documents which are either
events, or descriptions of events.  An ``event`` is the smallest quantum of data
stored in the metadata store and represents a *action* at a given time. For
example: "*measurement of 8 scaler chanels*", "*trigger detectors*" or
"*start run*". 

One of the cornerstones of this data acquisition and analysis method is the use
of *time* as the method by which data can be aligned and correlated. A single
``event`` should have happened at a certain quantum of time with the
determination of what a time *quantum* is left to the details of the
experiment. Time however, can be horrendously messy. Throughout this
section we use two terms, *timestamp* and *time*. These mean:

- *time* : The date/time as found at the client side when an ``event`` is
  created. This could be a date-time format as determined by the underlying
  storage method (for example a database)

- *timestamp* : A (usually float) representation of the hardware time when a
  certain value was obtained. Wherever possible this should be read from
  hardware. For example, this could be the *EPICS* timestamp from when the
  record processed which provides the value. 

In order to allow the *event* concept to be applied to many different events,
events have a type. These types indicate what happened at that time. These
event types are:

- *measure* : A measurement of data from external sources. For example,
  reading a scaler or taking a CCD image. 
- *trigger* : An event which occurred because data sources were triggered.
  For example, starting a scaler or CCD acquisition
- *start_run* : An event which is created when a data collection run starts.
- *end_run* : An event which is created when a data collection run ends. 

Events
======

Events are the smallest quantum of data stored in the metadatastore. They group
values which are associated with temporally identical data. The definition of
"temporally identical" is determined by the DAQ system. For example, the 32
channels in a scalar can be considered to be temporally identical because they
are hardware synchronized. Inclusion of a CCD image (with a reference to the
file store) can be included if this event is triggered at the same time, either
by software or hardware.  Each ``event`` contains the data values and a client
side timestamp of when the even was created. The same logic is applied to
``trigger events``. These are grouped with temporally identical triggers (again
determined by the DAQ philosophy).

Start and End Run Events
------------------------

The beginning of a data collection run creates an event which contains
sufficient metadata and information to describe the data collection. For
example, this is where beamline config information is located. The start run
event also serves as a searchable entity which links all data associated by an
event. For example::

    start_event_b : {
        "uid" : <uid>,
        "scan_id" : <non-unique-id>,
        "beamline_id: : <string>,
        "sample" : {
            "id" : <number>,
            "description" : <string>
        }
        "project" : <string>,
        "beamline_config" : {
            "diffractometer" : {
                "geometry" : <string>,
                "xtal" : {
                    "a" : <float>,
                    "b" : <float>,
                    "c" : <float>,
                    "alpha" : <float>,
                    "beta" : <float>,
                    "gamma" : <float>
                }
                "UB" : [...]
            }
        },
        "time" : <time>
    }

With the corresponding end run event as::

    end_run_event_c : {
        "uid" : <id>,
        "start_id" : <id>,
        "reason" : <string>,
        "time" : <time>
    }

where the reason can be used to describe why a run ended e.g. was it aborted or
was there an exception during data collection. The field ``start_id`` is a
pointer to the start event. 

.. _trigger_events:

Trigger Events and Event Descriptors
------------------------------------

Trigger events follow the same format as :ref:`measure_events` and
:ref:`measure_event_descriptors` with the exception that there is usually no
data associated with the trigger.

For example a trigger of a scaler and a CCD frame would be::

    event_trigger_a : {
        "uid" : <uid>,
        "data" : {
            "sclr" : {"timestamp" : <ts> }
            "ccd" : {"timestamp" : <ts> }
        }
        "time" : <time>,
    }

    event_trigger_descriptor_a : {
        "uid" : <uid>,
        "keys" : {
            "sclr" : {"dest" : "PV:XF:23ID1-ES{Sclr:1}.CNT", "value" : 1 } 
            "ccd" : {"dest" : "PV:XF:23ID1-ES{Dif-Cam:PIMTE}cam1:Acquire",
                     "value", 1 }
        }
        "run" : <uid>,
        "time" : <time>
    }

Where as before ``run`` is a pointer to the start run event. 

.. _measure_events:

Measure Events
--------------

Measure events contain the data measured at a certain instance in time or
explicit point in a sequence. Unlike :ref:`trigger_events` they contain actual
data. For example::

    measure_event_a : {
        "uid" : <uid>,
        "seqno" : <integer>,
        "ev_desc" : <uid>,
        "data" : {
            "chan1" : {"value" : <value>, "timestamp" : <ts>},
            "chan2" : {"value" : <value>, "timestamp" : <ts>},
            "chan3" : {"value" : <value>, "timestamp" : <ts>},
            "chan4" : {"value" : <value>, "timestamp" : <ts>},
            "chan5" : {"value" : <value>, "timestamp" : <ts>},
            "chan6" : {"value" : <value>, "timestamp" : <ts>},
            "chan7" : {"value" : <value>, "timestamp" : <ts>},
            "chan8" : {"value" : <value>, "timestamp" : <ts>},
            "pimte" : {"value" : <uid>, "timestamp" : <ts>}
        }
        "time" : <time>
    }

Where the keys ``uid``, ``ev_desc`` and ``timestamp`` refer to the unique id, a
link to the event descriptor and the EPICS timestamp respectively.

The following fields are considered essential:

- **uid** : Unique ID guaranteed to be unique.
- **ev_disk** : Reference to event descriptor.
- **time** : Client side time of event creation. 

The field **seqno** can be used by step-wise data collection to determine the
order of the events in a run.

.. _measure_event_descriptors:

Measure Event Descriptors
-------------------------

Event descriptors are used to describe an array of events which can form an
event stream of a collection of events. For example a run forms
event_descriptors at run start to define the data collected. For the example
above ``event`` is described by the ``event_descriptor`` ::

    event_desc_a : {
        "uid" : <uid>,
        "keys": : {
            "chan1" : {"source" : "PV:XF:23ID1-ES{Sclr:1}.S1"},
            "chan2" : {"source" : "PV:XF:23ID1-ES{Sclr:1}.S2"},
            "chan3" : {"source" : "PV:XF:23ID1-ES{Sclr:1}.S3"},
            "chan4" : {"source" : "PV:XF:23ID1-ES{Sclr:1}.S4"},
            "chan5" : {"source" : "PV:XF:23ID1-ES{Sclr:1}.S5"},
            "chan6" : {"source" : "PV:XF:23ID1-ES{Sclr:1}.S6"},
            "chan7" : {"source" : "PV:XF:23ID1-ES{Sclr:1}.S7"},
            "chan8" : {"source" : "PV:XF:23ID1-ES{Sclr:1}.S8"}, 
            "pimte: : {"source" : "FILESTORE:<...>"}
        },
        "run" : <uid>,
        "time" : <time>
    }





