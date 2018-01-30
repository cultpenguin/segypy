#!/usr/bin/env python
# testsegy.py

import segypy

filename='ld0077_file_0126.sgy';
filename='shotgather.sgy';

# Set verbose level
segypy.verbose=1;


SH = segypy.getSegyHeader(filename);


#%% Read Segy File
[Data,SH,STH]=segypy.readSegy(filename);

#%% Plot Segy filwe
scale=1e-9;
# wiggle plot
segypy.wiggle(Data,SH,1e-9);
# image plot
segypy.image(Data,SH,scale);

