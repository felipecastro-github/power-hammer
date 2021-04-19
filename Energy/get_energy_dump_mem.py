"""
Get signal energy, electrical energy and dump Turpial memory

file get_energy_dump_mem.py
Author: Felipe Castro
Date: 

THIS SOFTWARE IS PROVIDED BY OnChip-UIS 

Project: Glitch attack
Module: Get energy and dump memory 

How to use:
>>python get_energy_dump_mem.py clock_cycles frequency divider_fraction repeat_num
"""
import csv,sys,os,subprocess,time
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

[cycles,freq,frac,rep] = [float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4])]

time_mul=1e-9 			## Time multiplier
#time_mul=2.5e-9 

def get_wave():
	os.system('./owon-sds7102-protocol/owon-dump -f output.bin')	## To read a oscilloscope memory
	os.system('./owon-sds7102-protocol/owon-parse output.bin')		## To convert the data from .bin file to .csv file
	dataCH1=[]
	dataCH2=[]
	with open('output.csv') as csv_file:							## To read the data in .csv file
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			dataCH1.append(row[1])
			dataCH2.append(row[2])
		
	CH1=[float(i)*0.01 for i in dataCH1[1:len(dataCH1)-1]] 			## To eliminate the headers and creat a array with a CH1 data 
	CH2=[float(i)*0.01 for i in dataCH2[1:len(dataCH2)-1]] 			## To eliminate the headers and creat a array with a CH2 data
	t=np.linspace(0,len(CH1)*time_mul,len(CH1))						## Time array
	return(CH1,CH2,t)

## Get glitch wave
[CH1,CH2,time_g]=get_wave()																	## Glitch signal
os.system('python get_evidence.py '+str(cycles)+' '+str(freq)+' '+str(frac)+' '+str(rep)) 	## Save glitch wave

## Dump memory
os.chdir('../Test_dump_mem')																							## cd ./Test_dump_mem
start_time = time.time()																								
if(int(subprocess.getoutput('python dump_comp_mem.py').split('\n')[-1])):												## To check if the MCU memory is 0.K.
	os.system('mv differences.csv ./Evidence/Memory_'+str(int(freq/1e6))+'M_'+str(int(frac))+'_'+str(int(rep))+'.csv')	## If the MCU memory isn't 0.K save a file with the all memory data
	result_dump=1
else:
	result_dump=0
print("Elapsed time: "+str(time.time()-start_time)+" seconds")		
## Get standby
os.chdir('..')
os.system('./program.sh')													## Program turpial
subprocess.call(["python","glitch.py",str(49),str(-3.0),"1",str(freq)])		## Do a less posible duration glitch 
os.chdir('Energy')															## cd ./Energy
[CH1_s,CH2_s,time_s]=get_wave()	#Stb signal									## standby signal

## Get limts
a = 0
b = int(a+round((cycles/freq)/time_mul))+45		## Final limit glitch signal
b_s = int(a+round((1/freq)/time_mul))+45		## Final limit standby signal

##Get energy wave
VDD=np.average(CH1_s)											## VDD average
P = (np.array(CH1))*((np.array(CH2)-np.array(CH1))/10)			## Electric power in glitch
P_s = (np.array(CH1_s))*((np.array(CH2_s)-np.array(CH1_s))/10)	## Electric power in stb
E_s=integrate.simps(P_s[b_s:b_s+b],time_s[b_s:b_s+b])			## Energy in MCU normal work 
E_g=integrate.simps(P[a:b],time_g[a:b])							## Energy in MCU glitch
E_sig=integrate.simps((VDD-np.array(CH1[a:b]))**2,time_g[a:b])	## Signal energy
file=open('energy_dump_results.txt','w')
file.write(str(E_s)+','+str(E_g)+','+str(E_sig)+','+str(result_dump)) ## Save .txt file with glitch electical energy, standby electrical energy, glitch signal energy and 
file.close()

