import csv,sys
import numpy as np

[cycles,freq,frac,rep] = [float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4])]

time_mul=1e-9 

dataCH1=[]
dataCH2=[]
with open('output.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	for row in csv_reader:
		dataCH1.append(row[1])
		dataCH2.append(row[2])
		
CH1=(np.array(map(float,dataCH1[1:len(dataCH1)-1])))*(0.01) ##To eliminate the headers 
CH2=(np.array(map(float,dataCH2[1:len(dataCH2)-1])))*(0.01) ##To eliminate the headers
time=np.linspace(0,len(CH1)*time_mul,len(CH1))				##Time vector

all_data=[time,CH1,CH2]
data_to_save=zip(*all_data)

## Get limts
a = 0
b = int(a+round((cycles/freq)/time_mul))+45

file_name = './Evidence/'+str(int(freq/1e6))+'M_'+str(int(frac))+'_'+str(int(rep))+'.csv'

with open(file_name, mode='w') as data_file:
    data_writer = csv.writer(data_file, delimiter=',')
    data_writer.writerow([str(cycles),str(b),str(freq)])
    data_writer.writerows(data_to_save)
print(file_name)

