# L-11 Avionics (AV4)

This flight features a very sophisicated multi-part avionics stack.

**AV4** is roughly the 5th iteration of our rocket avionics.


# AV4 Overview

![AV4 Overview](AV4_overview.svg)

AV4 stackup:

 - **Main Flight Computer**
   - Intel Atom N455 PCI-104, 1.6 GHz
 - **Rocket Net Hub**
   - STM32 + KSZ8999
 - **IMU**
   - ADIS16405 (9DOF IMU)
   - MPU9150 (6DOF IMU)
   - MPL3115A2 (Baro)
 - **Roll Control**
   - JR Servo DS8717
 - **GPS**
   - GPS RF Front end recorder
   - Hemisphere Crescent OEM
 - **Battery**
   - 4 cell LiPo
   - BQ3060 SBS management chip
 - **Cameras**
   - Raspberry Pi Model B
   - Omnivision 5647 sensor


Info about Arm State [arm-state.markdown](arm-state.markdown) and
Programmable parts [programmable.markdown](programmable.markdown).


# Rocket Net Hub

The **R**ocket **N**et **H**ub is the central power and data distribution node
for the rocket. It contains an 8 port Ethernet switch and an STM32
microcontroller.

![RNH Overview](RNH_overview.svg)

### RNH API

Being the center of activity, the RNH will need to respond to many commands:

### List of RNH Commands

Command Port: `10.0.0.5:36100`
Response Port: `10.0.0.5:36101`

| Name              | Description                                     | Magic String                  | Return Value                         |
| ----------------- | ----------------------------------------------- | ----------------------------- | ------------------------------------ |
| Arm               | Puts the rocket in an armed state               | `#YOLO`                       | Success or failure and reason        |
| Safe              | Takes rocket out of arm state                   | `#SAFE`                       | Success                              |
| Power ON [port#]  | Turns on power to a port                        | `#ON_PN` [N=port number byte] | Success or failure and reason        |
| Power OFF [port#] | Turns off power to a port                       | `#FF_PN` [N=port number byte] | Success or failure and reason        |
| Version           | Return code version                             | `#VERS`                       | Code Version                         |
| Get Time          | Return the current master time (RNH Boot time)  | `#TIME`                       | Time and arm state                   |
| Power stats       | Return the current battery and power states     | `#POWR`                       | Battery charge level, ACOK, ON ports |
