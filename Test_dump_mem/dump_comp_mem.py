"""

Parla

"""
import os		# To call terminal comands

def dumpMemory(size):
	while(1):
		os.system("./mRISCVprog_test -u 0,"+size+" data.dat -v")	# Dump memory to .dat file
		os.system("od -t x4 -An -w4 -v data.dat > data.hex")		# Convert .dat to .hex
		file2=open('data.hex','rb') ##Open file						# Read the .tex file
		read_data=file2.read().split('\n')							# To list
		read_data.remove('')
		file2.close()												# Check that don't have Timeout's problems
		if(read_data[0] == ' 00000000'):
			print("Wrong reading!... Retrying")
		else:
			if(len(read_data)==int(size,16)):						# Check that the read data is complete
				break
			else:
				print("Wrong reading!... Retrying")
	return read_data

def main():	
	file1=open('../Assembly/glitch_attack.hex','rb') 					# Open the programing file
	real_data=file1.read().split('\n')
	file1.close()
	real_data.remove('')
	read_data=dumpMemory(hex(len(real_data))[2:])					# Get the DUT memory data
	if all(real_data[i]==read_data[i] for i in range(len(real_data))):	# Compare if the data is correct
		print(0)														
	else:																# if it isn't correct save .csv file with the differences
		print(1)
		diff_data=[hex(i)+","+real_data[i]+","+read_data[i]+"\n" for i in range(len(real_data)) if real_data[i] != read_data[i]] #get the rows whit differences
		file3=open('differences.csv','w')
		file3.write(''.join(diff_data)) #concat and write file
		file3.close()
		#Save file with differences
	os.system('rm data.dat')
	os.system('rm data.hex')


try:
	main()
except KeyboardInterrupt:
	os._exit()

