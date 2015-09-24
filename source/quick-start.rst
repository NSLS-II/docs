.. highlight:: bash
***************************
Data Collection Quick Start
***************************

Here we are assume that you are sitting at a beamline computer that has
the software installed and configured. If you need to start from the *very*
beginning, 

#. Log into your beamline user account, e.g., xf23id.
   
#. Activate the ``collection`` conda environment.::

    source activate collection

   This command makes the data collection software available by adding it
   your UNIX ``$PATH``.

#. Start IPython with a profile.::

    ipython --profile=collection

   A "profile" runs code at startup to define useful variables and
   functions, including the names of motors and detectors.

#. You are ready to work. For example, list all positioners.::

    In [1]: wh_pos()

    -------------------------------------------------------------------------------------
    | Positioner         | Value              | Low Limit          | High Limit         |
    -------------------------------------------------------------------------------------
    | bpm1_y             |  0.7269 mm         |  0.000000 mm       |  0.000000 mm       |
    | bpm2_ydiode        | -9.9956 mm         |  0.000000 mm       |  0.000000 mm       |
    | bpm2_yfoil         | -30.1198 mm        |  0.000000 mm       |  0.000000 mm       |
    | dlm_c1_bnd_bi      |  85000 au          |  0.000000 au       |  0.000000 au       |
    | dlm_c1_bnd_bo      |  88000 au          |  0.000000 au       |  0.000000 au       |
    | dlm_c1_bnd_ti      |  85000 au          |  0.000000 au       |  0.000000 au       |
    | dlm_c1_bnd_to      |  77000 au          |  0.000000 au       |  0.000000 au       |
    | dlm_c1_p           |  0.5465 deg        |  0.000000 deg      |  0.000000 deg      |
    | dlm_c1_xi          |  0 counts          |  0.000000 counts   |  90000.000000 counts |
    | dlm_c1_xo          | -1 counts          |  0.000000 counts   |  0.000000 counts   |
    ...
    -------------------------------------------------------------------------------------
