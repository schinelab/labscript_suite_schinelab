from labscript import *
from labscript_utils import import_or_reload
import numpy as np

# the dot in python acts as the folder slash here
import_or_reload('labscriptlib.Yb171_MOT_Tweezer_trap.connection_table')

start()

t=0

start_experiment.go_high(t)
t+=2e-3
start_experiment.go_low(t)
t+=3e-3
Blue_3D_MOT.go_high(t)
Zeeman_slower.go_high(t)
Blue_2D_MOT.go_high(t)
Green_Beams.go_high(t)
MOT_coils_setpoint.constant(t,B_INITIAL)

t+=TIME_UNTIL_RAMP
t+=RAMP_DURATION
add_time_marker(t, "Ramping magnetic field down", verbose=True,color='red')
t+=3e-3
cam1.expose(t, "before_ramp", trigger_duration=2e-3)
t+=MOT_coils_setpoint.ramp(t,duration=RAMP_DURATION,initial=B_INITIAL,final=B_FINAL,samplerate=1e4)
t+=3e-3    
add_time_marker(t, "Looking for only green MOT", verbose=True,color='red')
    
MOT_coils_setpoint.constant(t,B_FINAL)
Blue_3D_MOT.go_low(t)
Zeeman_slower.go_low(t)
Blue_2D_MOT.go_low(t)
    
t+=TIME_TO_TRIGGER_CAMERA_AFTER_RAMP
cam1.expose(t, "after ramp", trigger_duration=2e-3)
t+=3e-3
stop(t)