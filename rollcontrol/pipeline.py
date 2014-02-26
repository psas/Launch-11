#!/usr/bin/env python
import numpy
from scipy.integrate import simps
from scipy.signal import firwin, lfilter

# original data. See: <https://github.com/psas/flight_data-2010.10.17>
opal_file = '../../../data/flight_data-2010.10.17/opal/Opal_launch_rotated.csv'
roll_file = '../../../data/flight_data-2010.10.17/roll/raw/output_trim.csv'

opal_sample_rate =  128     # Hz
roll_sample_rate = 1000     # Hz

# filter design
freq_cuttoff = 10  # Hz, low pass
window = firwin(numtaps=20, cutoff=freq_cuttoff, nyq=opal_sample_rate/2)



# read in files
columns = numpy.loadtxt(opal_file, delimiter=',', unpack=True)

opal_time  = columns[0]
opal_accel = columns[3]
opal_rate  = columns[6]

# calculate velocity and angular acceleration
velocity = [0]
angular_accel = [0]
for i in range(len(opal_accel)):
    if i < len(opal_accel)-1:
        velocity.append(simps(opal_accel[:i+1], opal_time[:i+1]))
    if i > 0:
        angular_accel.append(opal_rate[i] - opal_rate[i-1])

velocity = numpy.array(velocity)
angular_accel = numpy.array(angular_accel)

# filter angular acceleation
angular_accel_filtered = lfilter(window, 1.0, angular_accel)




# write out to file
with open('model_data__.csv', 'w') as f_out:
    for i, t in enumerate(opal_time):
        f_out.write("%f,%f,%f,%f\n" % (t, angular_accel[i], angular_accel_filtered[i], velocity[i]))
