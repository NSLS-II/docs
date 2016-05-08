Understanding the contents of the header
****************************************

The databroker provides the metadata in a dictionary of names and values that
we call the *header*.

The header has three main pieces:

* the 'start' document, ``header['start']``, contains most of the interesting
  metadata -- everything we know before the run starts. (What kind of scan
  are we doing? Why? Who? When?)
* the 'stop' document, ``header['stop']``, contains what we only know when
  the scan is complete --- mainly, did it work?
* a list of 'descriptor' documents in ``header['descriptors']`` which serve
  a sort of table of contents, giving metadata about each field (PV name,
  data type, precision, units) and its configuration (e.g., exposure time).
