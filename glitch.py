#!/usr/bin/python

"""
ChipWhisperer glitch configuration

file python glitch.py
Author: Felipe Castro
Date: 

THIS SOFTWARE IS PROVIDED BY UIS 

Project: Glitch attack
Module: chipwhisperer glitch maker 

Rivision History:
0.1  - 20200101 - Initial version

// using:
>>python glitch.py glitch_width glitch_offset repeat(clock cycles) frequency
"""
import chipwhisperer as cw	## To use the chipwhisperers funtions
import time					## To calculate the excecutions times
import sys					## To use the arguments

[width,offset,repeat,freq] = [float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]),int(float(sys.argv[4]))]

try:
	scope = cw.scope()		## Create the chipwhisperer object
except NameError:
	pass

scope.clock.clkgen_src = "extclk"		## Select the clock source
scope.clock.extclk_freq = freq			## External clock frequency
scope.clock.adc_src = "clkgen_x4"		## FPGA ADC clock source
scope.trigger.triggers = "tio4"			## FPGA trigger pin
scope.io.tio1 = "serial_rx"				## FPGA gpio1
scope.io.tio2 = "serial_tx"  			## FPGA gpio2
scope.io.hs2 = "disabled"				## FPGA extra pin, could be pinout for clock

scope.io.tio3 = "gpio_low"				## FPGA gpio3, high to reset the edge detector 
scope.io.tio3 = "gpio_high"
scope.io.tio3 = "gpio_low"

scope.glitch.clk_src = 'target'			## Glitch module clock source (target,clkgen). In target the clock would be conected at pin HS1 
scope.glitch.output = "enable_only"		## Glitch output form (clock_only,glitch_only,clock_or,clock_xor,enable_only)
scope.glitch.ext_offset = 0				## External offset, wait for # clock cycles
scope.glitch.width = width				## Glitch with, one pulse can range from -49.8% to roughly 49.8% of a period. In enable_only it's not important, could be 49.
scope.glitch.width_fine = 0				## Fine adjust width [-255,255]
scope.glitch.offset = offset			## A pulse may begin anywhere from -49.8% to 49.8% away from a rising edge, allowing glitches to be swept over the entire clock cycle 
scope.glitch.offset_fine = 0			## Fine adjust offset [-255,255]
scope.glitch.trigger_src = "manual"		## Gltch trigger mode (continuous,manual,ext_single,ext_continuous)
scope.glitch.repeat = repeat			## Number of repetitions 
scope.io.glitch_hp = True				## Enable the high power N-MOS transistor
scope.arm()								## Do the glich(es). Setup scope to begin glitching when triggered.

