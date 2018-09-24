# Pmod-KYPD-Library
KYPDscanner version 1.0 9/23/18

Written by Adam Korycki 2018

This program is an open-source, object-oriented library for interfacing the PmodKYPD with the raspberry pi

Send bugreports, fixes, enhancements, t-shirts, money, beer & pizza to akorycki@ucsc.edu
__________________________________________________________________________________________________________
Hardware connections:

*+5V must be connected from the RPi's GPIO to pins 6 and 12 of the PmodKYPD 

*GND must be connected from the RPi's GPIO to pins 5 and 11 of the PmodKYPD

*pins 1-4 (columns 4-1) must be individually connected to 4 GPIO rails on the RPi

*pins 7-10 (rows 4-1) must be individually connected to 4 GPIO rails on the RPi

In total, there should be 12 wires connected between the RPi and PmodKYPD. Of which, 4 are either +5V or GND 
and the remaining 8 are individually connected to 8 seperate general-purpose IO pins on the RPi

__________________________________________________________________________________________________________
Software:

To initialize a GPIO connection between the RPi and PmodKYPD, an initialization method is used with the 
folowing parameters:

1) column 4 (RPi GPIO pin # connected to pin 1 on the PmodKYPD)
2) column 3 (RPi GPIO pin # connected to pin 2 on the PmodKYPD)
3) column 2 (RPi GPIO pin # connected to pin 3 on the PmodKYPD)
4) column 1 (RPi GPIO pin # connected to pin 4 on the PmodKYPD)
5) row 4 (RPi GPIO pin # connected to pin 7 on the PmodKYPD)
6) row 3 (RPi GPIO pin # connected to pin 8 on the PmodKYPD)
7) row 2 (RPi GPIO pin # connected to pin 9 on the PmodKYPD)
8) row 1 (RPi GPIO pin # connected to pin 10 on the PmodKYPD)

Below a KYPDscanner object named Pmod_scanner is initialized:

Pmod_scanner = KYPDscanner(8, 10, 12, 16, 18, 22, 24, 26)

Where pin 8 on the RPi is connected to column 4, or pin 1 on the PmodKYPD etc...

The current vesrion of the KYPDscanner library has 2 functions:

*begin() is a function which echos keypad input onto the terminal

*string() is a fuction which takes a series of keypad inputs and, when the letter 'E' is pressed, displays
it onto the terminal


Here is an example client program which utlizes the KYPDscanner library:

#####################################################

from KYPDscanner import KYPDscanner

PmodKYPD = KYPDscanner(8, 10, 12, 16, 18, 22, 24, 26)

PmodKYPD.begin()

#####################################################
