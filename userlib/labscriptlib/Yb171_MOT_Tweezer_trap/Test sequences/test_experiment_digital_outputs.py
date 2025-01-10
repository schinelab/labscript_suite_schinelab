from labscript import *
from labscript_utils import import_or_reload
import numpy as np

import_or_reload('labscriptlib.connection_table')

start()

t=0
ind=0

flag2test.go_high(t)


# while t<0.2:
#     flag1test.go_high(t)
#     if ind%2==0:
#         flag3test.go_high(t)
#     else:
#         flag3test.go_low(t)
#     t+=1e-2
#     flag1test.go_low(t)
#     t+=1e-2
#     ind += 1

dt=0.01
for ii,t in enumerate(np.arange(0,0.2,2*dt)):
    flag1test.go_high(t)
    if ii%4==0:
        flag3test.go_high(t)
    elif ii%4==1:
        flag4test.go_high(t)
    elif ii%4==2:
        flag3test.go_low(t)
    else:
        flag4test.go_low(t)

    t+=dt
    flag1test.go_low(t)
    t+=dt

t+=.25
# flag1test.go_high(t)
# t+=dt
# flag2test.go_low(t)
# t+=dt

flag1test.go_low(t)
flag2test.go_low(t)
flag3test.go_low(t)

stop(t)