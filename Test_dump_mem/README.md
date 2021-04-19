To dump the MCU complete memory you would compile and use a modifided mRISCVprog
 
Compile using:
```
gcc -Wall mRISCVprog_test.c greset.c -o mRISCVprog_test -L./ -lMPSSE -lftd2xx -ldl
gcc -Wall mRISCVprog_test.c greset.c -DGW32C -o mRISCVprog_test.exe -L./ -lMPSSE -lftd2xx -lgw32c -lintl-8
```
Execute it using:
```
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:./ ./mRISCVprog_test
```

