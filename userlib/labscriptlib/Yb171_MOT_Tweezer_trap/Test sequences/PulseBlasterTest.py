from labscript import *

from labscript_utils import import_or_reload
#from labscriptlib.common.functions import *

import_or_reload('labscriptlib.connection_table')

def initialize_test(t):
    # turn on pulse tester flag 7
    
    pulseTester.go_high(t)
    return(.02)

def return_to_defaults(t):
    
    pulseTester.go_low(t)

    return(.1)

################################################################################
#   Experiment Sequence
################################################################################

start()

t=0
while t<3.99e-3:
    clock.go_high(t)
    t+=1e-6
    clock.go_low(t)
    t+=1e-6

t+=initialize_test(0)
t+=return_to_defaults(t)


stop()