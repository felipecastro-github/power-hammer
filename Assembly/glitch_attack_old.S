.text;
.global _start;

#### BEGIN _start
_start:
	li s0, 0x1040;		# GPIO address
	add s1, zero, x0;	# GPIO status 1
	#ori s1, zero, 0x7;	# This is if you want strong driver
	sw s1, 0(s0);
	sw s1, 4(s0);
	sw s1, 8(s0);
	sw s1, 12(s0);
	sw s1, 16(s0);
	sw s1, 20(s0);
	sw s1, 24(s0);
	sw s1, 28(s0);
	add s1, zero, 0x3;
	sw s1, 0(s0);		# Write to GPIO 1

#.section .rodata
#.balign 4
#string1:
#	.string "n";
infinite:
	loop_1:
		sw s1, 4(s0);		# Write to GPIO 2
		#lui a0, %hi(string1);
		#addi a0, a0, %lo(string1);
		#call printf;
		#.string "n";
		jal zero, loop_1;
	loop_2:
		sw s1, 8(s0);		# Write to GPIO 3
		#xori s1, s1, 0x3;	# Toogle GPIO status
		jal zero, loop_2;
	loop_3:
		sw s1, 12(s0);		# Write to GPIO 4
		#xori s1, s1, 0x3;	# Toogle GPIO status
		jal zero, loop_3;
	loop_4:
		sw s1, 16(s0);		# Write to GPIO 5
		#xori s1, s1, 0x3;	# Toogle GPIO status
		jal zero, loop_4;
	loop_5:
		sw s1, 20(s0);		# Write to GPIO 6
		#xori s1, s1, 0x3;	# Toogle GPIO status
		jal zero, loop_5;
	loop_6:
		sw s1, 24(s0);		# Write to GPIO 7
		#xori s1, s1, 0x3;	# Toogle GPIO status
		jal zero, loop_6;
	loop_7:
		sw s1, 28(s0);		# Write to GPIO 8
		#xori s1, s1, 0x3;	# Toogle GPIO status
		jal zero, loop_7;

	jal zero, infinite;
	

#riscv32-unknown-elf-gcc -c glitch_attack.S
#riscv32-unknown-elf-objdump -d glitch_attack.o 
#riscv32-unknown-elf-gcc -Os -m32 -ffreestanding -nostdlib -o glitch_attack.elf -Wl,-Bstatic,-T,sections.lds,-Map,glitch_attack.map,--strip-debug glitch_attack.o -lgcc
#riscv32-unknown-elf-objcopy -O binary glitch_attack.elf glitch_attack.dat

