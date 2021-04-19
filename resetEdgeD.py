#!/usr/bin/python

import chipwhisperer as cw
import sys

[freq] = [float(sys.argv[1])]

try:
	scope = cw.scope()
	#self.scope=scope
	target=cw.target(scope)
	#self.target=target
except NameError:
	pass
"""
#scope.clock.freq_ctr_src="extclk"
scope.clock.clkgen_src = "system"
#scope.clock.clkgen_src = "extclk"
#scope.clock.extclk_freq = freq
scope.clock.clkgen_freq = freq
scope.clock.adc_src = "clkgen_x4"
scope.trigger.triggers = "tio4"
scope.io.tio1 = "serial_rx"
scope.io.tio2 = "serial_tx"
scope.io.hs2 = "clkgen"
"""
scope.io.tio3 = "gpio_low"
scope.io.tio3 = "gpio_high"
scope.io.tio3 = "gpio_low"
