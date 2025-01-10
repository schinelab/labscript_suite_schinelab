from labscript import *
from labscript_utils import import_or_reload
import numpy as np

# the dot in python acts as the folder slash here
import_or_reload('labscriptlib.Yb171_MOT_Tweezer_trap.connection_table')

start()

t=0
Zeeman_slower.go_high(t)
Blue_2D_MOT.go_high(t)
probe_beam.go_low(t)

t+=2
Zeeman_slower.go_low(t)
Blue_2D_MOT.go_low(t)
probe_beam.go_high(t)

t+=2
Zeeman_slower.go_high(t)
Blue_2D_MOT.go_high(t)
probe_beam.go_low(t)

t+=2
Zeeman_slower.go_high(t)
Blue_2D_MOT.go_high(t)
probe_beam.go_low(t)
stop(t)