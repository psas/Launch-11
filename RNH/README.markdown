# Rocket Net Hub

The **R**ocket **N**et **H**ub is the central power and data distribution node
for the rocket. It contains an 8 port Ethernet switch and an STM32
microcontroller.


![RNH Overview](http://psas.github.io/Launch-11/RNH/RNH_overview.svg)


## API

Being the center of activity, the RNH will need to respond to many commands.


### List of RNH Commands

Command Port: `TODO`

| Name              | Description                                     | Magic String                 | Return Value                         |
| ----------------- | ----------------------------------------------- | ---------------------------- | ------------------------------------ |
| Arm               | Puts the rocket in an armed state               | `#YOLO`                      | Success or failure and reason        |
| Safe              | Takes rocket out of arm state                   | `#SAFE`                      | Success                              |
| Power ON [port#]  | Turns on power to a port                        | `#ON_N` [N=port number byte] | Success or failure and reason        |
| Power OFF [port#] | Turns off power to a port                       | `#FF_N` [N=port number byte] | Success or failure and reason        |
| Version           | Return code version                             | `#VERS`                      | Code Version                         |
| Get Time          | Return the current master time (RNH Boot time)  | `#TIME`                      | Time and arm state                   |
| Power stats       | Return the current battery and power states     | `#POWR`                      | Battery charge level, ACOK, ON ports |
