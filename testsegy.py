#!/usr/bin/env python
#
# testsegy.py
#
#import struct;


import segypy
import matplotlib.pylab as plt

#%%

#filename='ld0077_file_0126.sgy';
filename='shotgather.sgy';
#filename='mini.sgy'
#filename='data_IEEE.segy';
#filename='data_IBM_REV1.segy';
#filename='data_IBM_REV0.segy';
#filename='data_1byteINT.segy';
#filename='data_2byteINT.segy';
#filename='data_4byteINT.segy';

# Set verbose level
segypy.verbose=1;


SH = segypy.getSegyHeader(filename);


#%% Read Segy File
[Data,SH,STH]=segypy.readSegy(filename);

#%%
plt.pcolor(Data)
plt.show();

#
#segypy.wiggle(Data,SH);

