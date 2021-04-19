// Glitch attack of Turpial
// By: Whoever Luis made in charge of this (Shouts)
// Adaptation by: Ckristian Duran
// Only rename the _start to main, then use better registers
// From the programmer's perspective, it will have 
// the BSS initialization, and the init call, before
// calling this function. Compile using:
// make software PROGRAM=glitch_attack BOARD=turpial LINK_TARGET=ram RISCV_PATH=/opt/riscv32im
#include <encoding.h>

  .section .text
  .globl main
  .type main,@function

#### BEGIN main
main:
  li a1, 0x1040;          // GPIO address
  //add a1, zero, x0;     // Huh? If you need a zero, then write a zero in the SW
  //ori a1, zero, 0x7;    // This is if you want strong driver
  sw zero, 0(a1);         // Zeroize GPIO 0
  sw zero, 4(a1);         // Zeroize GPIO 1
  sw zero, 8(a1);         // Zeroize GPIO 2
  sw zero, 12(a1);        // Zeroize GPIO 3
  sw zero, 16(a1);        // Zeroize GPIO 4
  sw zero, 20(a1);        // Zeroize GPIO 5
  sw zero, 24(a1);        // Zeroize GPIO 6
  sw zero, 28(a1);        // Zeroize GPIO 7
  addi a2, zero, 0x3;     // Make a1 <- 3
  sw a2, 0(a1);           // GPIO 1 ON

infinite:
  loop_1:
    sw a2, 4(a1);         // Write to GPIO 1
    la a0, string1;     // You can use these two instructions
    call print_str;     // To use the included print_str
    //li a0, 0x1040       // Need to redefine those if use print_str
    //li a1, 0x3
    //xori a1, a1, 0x3;   // Toogle GPIO status
    jal zero, loop_1;     // Trap the execution in loop_1
  loop_2:
    sw a2, 8(a1);         // Write to GPIO 2
    la a0, string2;     // You can use these two instructions
    call print_str;
    //xori a1, a1, 0x3;   // Toogle GPIO status
    jal zero, loop_2;     // Trap the execution in loop_2
  loop_3:
    sw a2, 12(a1);
    la a0, string2;     // You can use these two instructions
    call print_str;        // Write to GPIO 3
    //xori a1, a1, 0x3;   // Toogle GPIO status
    jal zero, loop_3;     // Trap the execution in loop_3
  loop_4:
    sw a2, 16(a1);  
    la a0, string2;     // You can use these two instructions
    call print_str;      // Write to GPIO 4    
    //xori a1, a1, 0x3;   // Toogle GPIO status
    jal zero, loop_4;     // Trap the execution in loop_4
  loop_5:
    sw a2, 20(a1);        // Write to GPIO 5
    la a0, string2;     // You can use these two instructions
    call print_str;
    //xori a1, a1, 0x3;   // Toogle GPIO status
    jal zero, loop_5;     // Trap the execution in loop_5
  loop_6:
    sw a2, 24(a1);        // Write to GPIO 6
    la a0, string2;     // You can use these two instructions
    call print_str;
    //xori a1, a1, 0x3;   // Toogle GPIO status
    jal zero, loop_6;     // Trap the execution in loop_6
  loop_7:
    sw a2, 28(a1);        // Write to GPIO 7
    la a0, string2;     // You can use these two instructions
    call print_str;
    //xori a1, a1, 0x3;   // Toogle GPIO status
    jal zero, loop_7;     // Trap the execution in loop_7

  jal zero, infinite;

.section .rodata
.balign 4
string1:
	.string "n";
string2:
	.string "s";

