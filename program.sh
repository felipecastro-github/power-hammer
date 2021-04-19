#!/bin/bash

#python config_clock.py

rmmod ftdi_sio
rmmod usb_serial

./mRISCVprog -v -h ./Assembly/glitch_attack.dat
#./mRISCVprog -v ./tests/glitch_attack.hex
#./mRISCVprog -v -h ./tests/print.dat
