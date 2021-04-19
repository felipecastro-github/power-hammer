#!/bin/bash

# To use
## ./compiletest.sh name_of_.S_file
## Ex. ./compiletest.sh giltch_attack

riscv32-unknown-elf-gcc -c $1.S
riscv32-unknown-elf-objdump -d $1.o 
riscv32-unknown-elf-gcc -O -ffreestanding -nostdlib -o $1.elf -Wl,-Bstatic,-T,sections.lds,-Map,$1.map,--strip-debug $1.o -lgcc
riscv32-unknown-elf-objcopy -O binary $1.elf $1.dat
od -t x4 -An -w4 -v $1.dat > $1.hex

	
