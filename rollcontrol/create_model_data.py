#!/usr/bin/env python
from scipy.integrate import simps
from scipy.signal import firwin, lfilter

# filter design
N = 10
freq_cuttoff = 10
freq = 128
window = firwin(numtaps=N, cutoff=freq_cuttoff, nyq=freq/2)

# init
vel = 0         # velocity, m/s
rot = 0         # angular acceleratioin, degrees/s

# list container for parsed data from file
times = [0]
accls = [0]
vels = [0]
rates = [0]
angular = [0]

# see https://github.com/psas/flight_data-2010.10.17 
with open('../../../data/flight_data-2010.10.17/opal/Opal_launch_rotated.csv', 'r') as f_in:


    for line in f_in:
        li = line.split(',')

        # we only care about time, z-acceleration, and roll rate
        time = float(li[0])
        accl = float(li[3])
        rate = float(li[6])

        times.append(time)
        accls.append(accl)
        rates.append(rate)

        # integrate accl to velocity
        vels.append( simps(accls, times) )
        angular.append( rate - rates[-2])

        #print time, vels[-1], rate, anglar[-1]


angular_filt = lfilter(window, 1.0, angular)

with open('model_data.csv', 'w') as f_out:

    for i, time in enumerate(times):

        f_out.write("%f,%f,%f,%f,%f,%f\n" % (time, vels[i], angular[i], angular_filt[i], accls[i], rates[i]))


