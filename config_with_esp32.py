"""
CY22150 i2c clock program using esp32

file python config_with_esp32.py
Author: Felipe Castro
Date: 

THIS SOFTWARE IS PROVIDED BY UIS 

Project: Glitch attack
Module: Resistor divider and clock(PLL) config 

How to use:
- Program the esp32 device using the code ./CY22150_intf_i2c.ino
- Run this script -> ptython CY22150_prog_esp32.py


iI2C_DEVICE_ADDRESS_EEPROM       0x69    # For PLL Clock EEPROM
"""	

import serial, time, sys
import serial.tools.list_ports

def writeReg(regaddr,data):
	#Functon to write each one of the config registers of PLL
	stx.write(bytearray([1,regaddr ,data]))
	#time.sleep(0.1)
	
pb_var=int(sys.argv[1])
frac=int(sys.argv[2])

for port in serial.tools.list_ports.comports():						## To search all common ports
	if(port.description == 'CP2102 USB to UART Bridge Controller'): ## I choise description because the serial number is not clear
		stx = serial.Serial(port.device,115200)						## Conect with esp32 using serial port
		

""" Clock EEPROM parameters"""
REF =               30000   # Reference clock In kHz
IS_ESR_30 =         1       # Crystal ESR is 30ohm?
XCL =               12      # Crystal Load Capacitance (in pF)
IS_EXTERNAL =       0       # 1/0 External Clock?
CLKOE_CLK6 =        0       # 1/0 Activate (CLK6)
CLKOE_CLK5 =        0       # 1/0 Activate (CLK5)
CLKOE_LCLK4 =       0       # 1/0 Activate (LCLK4)
CLKOE_LCLK3 =       0       # 1/0 Activate (LCLK3)
CLKOE_LCLK2 =       0       # 1/0 Activate (LCLK2)
CLKOE_LCLK1 =       1       # 1/0 Activate (LCLK1)
DIV1SRC =           0       # 1-bit DIV1 Muxer
DIV1N = 	   		20      # 7-bit DIV1 Divider (Min 4)
PB =                pb_var  # 10-bit PB Counter
PO =                0       # 1-bit PO Counter
Q =                 1       # 7-bit Q Counter
CLKSRC_LCLK1 =      1       # 3-bit Crosspoint switch matrix control (LCLK1)
CLKSRC_LCLK2 =      0       # 3-bit   switch matrix control (LCLK2)
CLKSRC_LCLK3 =      0       # 3-bit Crosspoint switch matrix control (LCLK3)
CLKSRC_LCLK4 =      0       # 3-bit Crosspoint switch matrix control (LCLK4)	
CLKSRC_CLK5 =       0       # 3-bit Crosspoint switch matrix control (CLK5)
CLKSRC_CLK6 =       0       # 3-bit Crosspoint switch matrix control (CLK6)
DIV2SRC =           0       # 1-bit DIV2 Muxer
DIV2N =             4       # 7-bit DIV2 Divider (Min 4)

""" Clock EEPROM parameters calculables"""
XDRV =        0        # 2-bit Input crystal oscillator drive control
CAPLOAD =     0        # 8-bit Input load capacitor control
PUMP =        0        # 3-bit Charge Pump

P=(2*(PB+4)+PO)
postDivider=DIV1N
CLK=((REF*P)/(Q+2))/postDivider  ## Final frequency
print ('Frequency: ',CLK*1000)

""" Register definition """
REG_09H = ((CLKOE_CLK6 << 5) | (CLKOE_CLK5 << 4) | (CLKOE_LCLK4 << 3) | (CLKOE_LCLK3 << 2) | (CLKOE_LCLK2 << 1) | (CLKOE_LCLK1))
REG_0CH = ((DIV1SRC << 7) | (DIV1N))
REG_12H = ((1 << 5) | (XDRV << 3))
REG_13H = (CAPLOAD)
REG_40H = ((0xC0) | (PUMP << 2) | ((PB >> 8) & 0x2))
REG_41H = (PB & 0xFF)
REG_42H = ((PO << 7) | (Q))
REG_44H = ((CLKSRC_LCLK1 << 5) | (CLKSRC_LCLK2 << 2) | ((CLKSRC_LCLK3 >> 1) & 0x2))
REG_45H = (((CLKSRC_LCLK3 & 0x1) << 7) | (CLKSRC_LCLK4 << 4) | (CLKSRC_CLK5 << 1) | ((CLKSRC_CLK6 >> 2) & 0x1))
REG_46H = (((CLKSRC_CLK6 & 0x2) << 6) | 0x3F)
REG_47H = ((DIV2SRC << 7) | (DIV2N))

""" Simple Macro-formula definitions"""
#CapLoad(C_L,C_BRD,C_CHIP) = ((C_L-C_BRD-C_CHIP)/0.09375)
#Q_TOTAL = (Q+2)
#P_TOTAL = ((2*(PB+4)) + PO)

### Write the PLL config registers
writeReg(0x09,REG_09H)
writeReg(0x0C,REG_0CH)
writeReg(0x12,REG_12H)
writeReg(0x13,REG_13H)
writeReg(0x40,REG_40H)
writeReg(0x41,REG_41H)
writeReg(0x42,REG_42H)
writeReg(0x44,REG_44H)
writeReg(0x45,REG_45H)
writeReg(0x46,REG_46H)
writeReg(0x47,REG_47H)

stx.write(bytearray([2, frac, 0]))	## Config the transistors of divider
stx.close()							## Close the serial port


