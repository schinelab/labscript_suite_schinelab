from labscript import *
from labscript_utils import import_or_reload
import numpy as np

import_or_reload('labscriptlib.connection_table')


#test0.ramp(t=0.1,duration=0.1,initial=0,final=5,samplerate=1e5)
#test0.ramp(t=0.2,duration=0.1,initial=5,final=0,samplerate=1e5)



t = 0
ind=0
#MOT_coils_power.go_high(t,2,units='V')
add_time_marker(t, "Start", verbose=True)
start()

#delay
t+=0.01

# initialize 
aom.go_low(t)
tweezers.go_low(t)
tweezers.go_high(0.01)

while t<0.3:
    aom.go_high(t)
    t+=1e-2
    aom.go_low(t)
    t+=1e-2
    ind+=1
aom.go_low(t)
# scope trigger

t += 0.1
add_time_marker(t, "Exposure: 'before' image", verbose=True)
field_ramp.ramp(t,duration=0.1,initial=0,final=5,samplerate=1e5)
field_ramp.ramp(t+0.1,duration=0.1,initial=5,final=0,samplerate=1e5)

tweezers.go_high(0.2)
tweezers.go_low(t)


t += 0.4
add_time_marker(t, "Exposure: 'after' image", verbose=True)
field_ramp.ramp(t,duration=0.1,initial=0,final=2,samplerate=1e5)
field_ramp.ramp(t,duration=0.1,initial=2,final=0,samplerate=1e5)


stop(1)



#creates a sawtooth ramp 
#for ii,t in enumerate(np.arange(0,0.9,0.1)):
#    t += test0.ramp(t, duration=0.1, initial=0, final=5, samplerate=1e5)
#    t += test0.ramp(t+0.1, duration=0.1, initial=5, final=0, samplerate=1e5)
#

