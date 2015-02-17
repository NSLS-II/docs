Deploying metadatastore
-----------------------

Lessons learned from SRX and CSX
================================

Beamlines will have /DATA and /POOL data storage. /DATA seems to be for
experimental data and /POOL for analysis.  SRX and CSX have opted to run the
mongo database daemon on the channel archiver server (xf05id-ca1, xf23id-ca).
This seems to be a reasonable setup and will be repeated on other beamlines
until someone provides a better option.  We found it useful to set up an alias
as CSX called 'xf23id-broker' that metadatastore and filestore could point to
so that they dont actually care which machine the mongodb daemon is running on.
We should do the same for SRX and all future beamlines, unless a better option
is presented.  Contact Petkus to do this.

Proposed Deployment Strategy
============================

#. Set up an alias at beamline for the server running the mongo daemon
   (xf##id-broker)
#. Install and configuration of mongodb on xf##id-broker

    #. Install mongodb on xf##id-broker::

        sudo apt-get install mongodb

    #. Edit /etc/mongodb.conf so that ``dbpath=/DATA/mongodb/`` and
       ``bind_ip = 0.0.0.0``
    #. Make the directory ``/DATA/mongodb/``
    #. Edit the permissions of ``/DATA/mongodb/`` so that the mongo daemon can write
       to this location: ``sudo chown -R mongodb:mongodb /DATA/mongodb``
    #. Restart the monogo daemon: ``sudo service mongodb restart``

#. Install metadatstore on a beamline computer. Note: This section of the guide
   assumes you have already installed anaconda or miniconda and set them up to
   talk to the NSLS-II binstar

    #. Activate whatever environment was set up: ``source activate <env_name>``
    #. Install metadatastore: ``conda install metadatastore -y``

#. Testing metadatastore installation

    #. **Option 1.** Use ``ophyd`` to perform a scan and ``databroker`` to
       retrieve the scan data.
    #. **Option 2.** Insert synthetic data into metadatastore (change the
       database name!!) and retrieve it with databroker.
