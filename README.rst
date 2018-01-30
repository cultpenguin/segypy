
.. image:: https://img.shields.io/pypi/v/segypy.svg?style=flat-square
    :target: https://pypi.org/project/segypy

.. image:: https://img.shields.io/pypi/pyversions/segypy.svg?style=flat-square
    :target: https://pypi.org/project/segypy

.. image:: https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square
    :target: https://en.wikipedia.org/wiki/MIT_License


SegyPY : A Python module for reading/writing of SEG-Y formatted files
=======================================================================
Copyright (C) 2005-2018 Thomas Mejer Hansen, thomas.mejer.hansen@gmail.com

Currently you can READ IBM Floats, IEEE, 1, 2 and 4 byte INTEGER formatted data, and WRITE anything but IBM Floats.

ACKNOWLEDGEMENT 
_______________
Secchi Angelo (with Howard Lightstone and Anton Vredegoor): The Ibm2Ieee conversion routines are developed and made availabe for SegyPY by

Pete Forman

Andrew Squelch. Extensive reformatting from version 0.3.0 to 0.3.1

Example
_____________


.. code:: 

   import segypy
 
   # Set verbose level
   segypy.verbose=1;
   
   filename='shotgather.sgy';
   
   # Get only SegyHeader
   SH = segypy.getSegyHeader(filename);
   
   
   #  Read Segy File
   [Data,SH,STH]=segypy.readSegy(filename);
   
   # Plot Segy file
   scale=1e-9;
   
   # wiggle plot
   segypy.wiggle(Data,SH,1e-9);
   # image plot
   segypy.image(Data,SH,scale);


