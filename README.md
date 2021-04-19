# power-hammer
This repository contains the scripts to measurement and test the effect of power supply glitches in TURPIAL microprocessor.

To work on this project, please clone the git project:
```
git clone https://github.com/felipecastro-github/power-hammer.git`
````
##DISTRIBUTION TREE
power-hammer
├── Energy
|	└── owon-sds7102-protocol
|	└── get_energy_dump_mem.py
|	└── get_evidence.py
├── Test_dump_mem
|	└── dump_comp_mem.py
|	└── ftd2xx.dll
|	└── ftd2xx.h
|	└── greset.c
|	└── greset.h
|	└── libMPSSE.dll
|	└── libMPSSE_spi.h
|	└── mRISCVprog_test
|	└── mRISCVprog_test.c
|	└── README.md
|	└── WinTypes.h
├── Assembly
|	└── compiletest.sh
|	└── glitch_attack.dat
|	└── glitch_attack.elf
|	└── glitch_attack.hex
|	└── glitch_attack.map
|	└── glitch_attack.o
|	└── glitch_attack.S
|	└── glitch_attack_ck.S
|	└── glitch_attack_old.S
|	└── sections.lds
├── config_with_esp32.py
├── glitch.py
├── resetEdgeD.py
├── mRISCVprog
├── program.sh
├── README.md
└── <strong>glitch_attack.py</strong>
##FOLDERS
###Energy
###Test_dump_mem
###Assembly

##FILES

##NOTES
