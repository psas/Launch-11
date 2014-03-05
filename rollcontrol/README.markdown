# Roll Control Theory

The first thing we need to do is create a model and validate it on past
launches.

`create_model_data.py` was written to take data from the succesful
[2010 roll control launch](https://github.com/psas/flight_data-2010.10.17)
and find the rocket's airspeed and angular acceleration for the duration of the
flight. These are imputs to the model.

## Discussion

`model_data_view.ipynb` is an ipython notebook that can be seen rendered on
[nbviewer.ipython.org](http://nbviewer.ipython.org/url/psas.github.io/Launch-11/rollcontrol/model_data_view.ipynb?create=1).


### `model_data.csv` format:

Columns:

 1. time [s]
 1. angular acceleration [&deg;/s/s]
 1. velocity [m/s]
 1. altitude [m]
 1. fin angle [aproximate angle in radians]
 1. roll rate [&deg;/s]
 1. acceleration (opal IMU) [m/s/s]
 1. acceleration (roll IMU) [ADC counts, mean = 0]
