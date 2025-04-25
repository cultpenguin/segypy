#!/usr/bin/env python
# testsegy.py

#%% 
import segypy
import matplotlib.pyplot as plt

filename='ld0077_file_0126.sgy'
filename='shotgather.sgy'

# Set verbose level
segypy.verbose=1

#%% Read only SegyHeader and SegyTraceHeader
SH = segypy.getSegyHeader(filename)
STH = segypy.getAllSegyTraceHeaders(SH)

#%% Read Segy File
[Data,SH,STH]=segypy.readSegy(filename)


#%% Plot Segy filwe
scale=1e-9
# wiggle plot
segypy.wiggle(Data,SH,1e-9)
# image plot
segypy.image(Data,SH,scale)
# invert y axis
plt.gca().invert_yaxis()
plt.title('Shot gather')
plt.xlabel('Trace number')
plt.ylabel('Time (s)')
plt.show()
#%% Plot Segy file with custom colormap
# colormap
cmap = plt.get_cmap('seismic')
# wiggle plot
segypy.wiggle(Data,SH, 1e-9)
plt.xlim(0, Data.shape[1])
# image plot

