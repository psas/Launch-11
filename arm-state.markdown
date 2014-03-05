# Rocket Arm State

Nearly all devices on the rocket are stateless. If something is powered it is
expected to perform fully. However there are a few exceptions:


### Rocket Net Hub

The rocket net hub (RNH) by default turns on, boots the STM32 and ethernet
switch, but none of the ports are given power. Commands can be issued to
turn on one port at a time. Additionally the RNH can be set into low power
mode where it will turn off the switch and only draw a few milliamps.


### Servo Enable

While the roll servo board is stateless, commands sent to it include a servo
disable bit. The flight computer (FC) is responsible for setting the enable
state, but itself only sets it if asked (of by virtue of launch detect).


# arm/unarmed/safe/off

Having the rocket **armed** implies that it is ready to launch, and airworthy.

If the rocket is on, but not armed, it is considered **unarmed**. The rocket can
also be **_safe_**, which means there are no dangerous items powered (for
instance the roll servo board).

If all ports on the rockets are off, then the rocket is considered '**off**'.

    arm > unarmed > safe > off [> phsically off, requires disconecting battery]


# Requirements for ARM

 - All ports on
 - GPS Lock
 - Shore Power OFF
