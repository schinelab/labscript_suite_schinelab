from labscript import *
from labscript_utils import import_or_reload
import numpy as np

import_or_reload('labscriptlib.connection_table')


#test0.ramp(t=0.1,duration=0.1,initial=0,final=5,samplerate=1e5)
#test0.ramp(t=0.2,duration=0.1,initial=5,final=0,samplerate=1e5)

t = 0
ind=0

start()

#for ii,t in enumerate(np.arange(0,0.90,0.1)):
#    t+= field_ramp.ramp(t,duration=50e-3,initial=20e-3,final=80e-3,samplerate=100)
#t+=200e-3
#initialize_experiment.go_low(200e-3)
#t+=field_ramp.ramp(t,duration=500e-3,initial=200e-3,final=800e-3,samplerate=100)

# initialize 
aom.go_low(t)
t+=10e-3
initialize_experiment.go_high(t)
add_time_marker(t, "Experiment start", verbose=True)
t+=10e-3
initialize_experiment.go_low(t)

add_time_marker(t, "Turning on slow ramp", verbose=True)
t+=field_ramp.ramp(t,duration=0.1,initial=0,final=5,samplerate=1e5)
t+=field_ramp.ramp(t,duration=0.15,initial=5,final=5,samplerate=1e5)
add_time_marker(t, "Rapid ramp down", verbose=True)
t+=field_ramp.ramp(t,duration=0.05,initial=5,final=0,samplerate=1e5)

tweezers.go_high(t)
while t<0.5:
    aom.go_high(t)
    t+=5e-3
    aom.go_low(t)
    t+=5e-3
    ind+=1
# scope trigger
tweezers.go_low(t)
t += 0.01


#field_ramp.ramp(t,duration=0.1,initial=0,final=2,samplerate=1e5)
#field_ramp.ramp(t,duration=0.1,initial=2,final=0,samplerate=1e5)


stop(0.600)



#creates a sawtooth ramp 
#for ii,t in enumerate(np.arange(0,0.9,0.1)):
#    t += test0.ramp(t, duration=0.1, initial=0, final=5, samplerate=1e5)
#    t += test0.ramp(t+0.1, duration=0.1, initial=5, final=0, samplerate=1e5)
#

