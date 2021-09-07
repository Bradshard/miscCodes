import pandas as pd
import random
import math
import matplotlib.pyplot as plt
import numpy as np

def tuples(x,y): # tuple making function for ease of access.
	a = []
	if len(x) == len(y):
		for i in range(len(y)):
			a.append((x[i],y[i]))
	else:
		print('give me equal length lists.')

	return a

def sampling(i,n): # sampling to create randomness.
	if ((len(i) is not 0 and len(n) is not 0) and (len(i) is not 1 and len(n) is not 1)):
		sample = random.sample(range(int(100000*i[-2]), int(100000*i[-1])), abs(n[-2]-n[-1]))
		# multiplied with 100000 to have fit enough values in sampling. 
		sample = [x/100000 for x in sample]
		return sample
	else:
		print('Values advancing or not enough data to sample (more than 1 needed). \n')

def mean_find(n,y,x): # pre-processor for sampling to make means
	mean = []
	length = []
	log_R = [] # values before the first 3 measurement errors not excluded
	ex_log_R = [] # values after the first 3 measurement errors excluded
	#ex_mean = []
	for i in range(len(n)):
		if ((n[i] is not None) and (len(n[i]) != 0)):
			log_R.append(((y[i]/real_muon_lifetime)+math.log(x[i]/y[i]))/y[i])
			mean.append(sum(n[i])/len(n[i]))
			length.append(len(n[i]))

	for i in range(3,len(log_R)):
		ex_log_R.append(log_R[i])

	#for i in range(0,len(mean)-3):
		#ex_mean.append(mean[i])  Used to experiment if statistical approach changes with exclusion of data.

	return mean, length, log_R, ex_log_R

def real_mean_calculator(i,x): # pre_processed means in their interval are processed to produce one mean
	total_len = 0
	total_microsec = 0
	mean = 0
	for z in range(len(i)):
		total_microsec += i[z]*x[z]
		total_len += x[z]
	mean = total_microsec/total_len
	print('total_microsec {} microseconds.'.format(round(total_microsec,1))) 
	# since real value has one(1) decimal point
	print('total_length {} units.\n'.format(total_len))
	return round(mean,1) # since real value has one(1) decimal point


def standard_dev(n,i): # to find standard deviation
	standard_dev = 0
	for k in i:
		standard_dev +=  k-n
	standard_dev = standard_dev/(len(i)-1)
	standard_dev = math.sqrt(standard_dev)  
	return round(standard_dev,1) # since real value has one(1) decimal point


colnames = ['Time(microsecond)', 'Muon Count'] # giving names to Dataframe.
data = pd.read_csv('Burkan-cosmic-muon-lifetime-data.csv', names = colnames, header = None)

df = pd.DataFrame(data) # turning csv into dataframes for convenience in turning to lists

pre_time = df['Time(microsecond)'].tolist() # before deleting header of the time column in list
time = [] # full list version after header of time.
pre_count = df['Muon Count'].tolist() # before deleting header of the muon count column in list
count = [] # full list version after header of count.

real_muon_lifetime = 2.2 # according to nyu, wikipedia and so.
error_point = 0 # for simplicity

samples = [] # sampling values in tuples for each data.
rem = [] # take the time values from the tuple to use in sampling
mu_rem = [] # take the muon count values from the tuple to use in sampling

for i in range(1,len(pre_time)):
	time.append(float(pre_time[i])) # the process into turning to lists without header

for i in range(1,len(pre_count)):
	count.append(int(pre_count[i])) # the process into turning to lists without header

time_count = tuples(time,count) # Tuple of microsecond, muon count, more convenient than lists.
#print(time_count)

for i in time_count:
	mu_rem.append(i[1])
	rem.append(i[0])
	samples.append((sampling(rem,mu_rem)))

#print(samples)


pre_mean, pre_length, pre_Log_R, pre_ex_log_r = mean_find(samples,time,count)
#print(pre_mean) # mean lifetime for each list
#print(pre_length) # counts in that lifetime of list
#print(pre_Log_R) # measuring with R = R_0*e**(-t/T)

mean = real_mean_calculator(pre_mean,pre_length) # Statistical approach on the mean lifetime

#ex_mean = real_mean_calculator(pre_mean,pre_length) # to see if statistical approach has error. None found.
#print(ex_mean)

standard_deviation = standard_dev(mean,rem) # standard deviation
"""
Two different scenarios.
"""
log_r = real_mean_calculator(pre_Log_R, pre_length)
excluded_log_r = real_mean_calculator(pre_ex_log_r, pre_length)


standard_deviation_log_r = standard_dev(log_r,rem)
standard_deviation_excluded_log_r = standard_dev(excluded_log_r,rem)


for i in range(len(rem)):
	if (mean==rem[i]):
		error_point = mu_rem[i]

for i in range(len(rem)):
	if (log_r == rem[i]):
		error_point_2 = mu_rem[i]

for i in range(len(rem)):
	if (excluded_log_r == (rem[i]-0.1)):
		error_point_3 = (mu_rem[i]+mu_rem[i-1])/2

error = 100*((mean-real_muon_lifetime)/real_muon_lifetime) # error between real and experimental
error_log_r = 100*((log_r-real_muon_lifetime)/real_muon_lifetime) # error between real and experimental(log_r)
error_ex_log_r = 100*((excluded_log_r-real_muon_lifetime)/real_muon_lifetime) # error between real and experimental(excluded_log_r)

# Decay-Fit

decay_func_fit = [] # decay function fit
n_0 = count[0] # to show to decay function on the fit 
time_fit = np.linspace(0,10,1000) # Not accurate but representative
for i in time_fit:
	decay_func_fit.append(n_0*math.e**(-i/real_muon_lifetime))


#Print values

print('mean lifetime experimental is equal to {}'.format(mean)) # mean lifetime
print('standard_deviation of experimental data is equal to {} \n'.format(standard_deviation)) # standard deviation lifetime

#For different experiments

print('mean(log-scale) lifetime experimental (activity formula applied) is equal to {}'.format(log_r)) # mean lifetime
print('standard_deviation(log-scale) of experimental data is equal to {} \n'.format(standard_deviation_log_r)) # standard deviation in log_r lifetime

#For different experiments

print('mean(error-deduced-log-scale) lifetime experimental (activity formula applied) is equal to {}'.format(excluded_log_r)) # mean lifetime (w/ error exclusion)
print('standard_deviation(log-scale with exclusion) of experimental data is equal to {}\n'.format(standard_deviation_excluded_log_r)) # standard deviation in log_r lifetime (w/ error exclusion)

# Plotting

plt.figure(1) # first figure 
plt.plot(rem,mu_rem, label = u"Muon Count vs Microseconds (\u03bcs)", color= 'navy', alpha = 0.75)
plt.plot(time_fit,decay_func_fit, label = "Decay Fit", color= 'orange', alpha= 0.75, ls= '--')
plt.axvline(x= mean, label= u"Mean lifetime experimental {} \u03bcs".format(mean) ,color= 'red', ls = '--')
plt.axvline(x= real_muon_lifetime, label= u"Mean lifetime actual {} \u03bcs".format(real_muon_lifetime) ,color= 'purple', ls= '--')
plt.title("Muon Lifetime Measurement")
plt.xlabel(u"Microseconds (\u03bcs)")
plt.ylabel("Muon Count")
plt.errorbar(mean, error_point, xerr= standard_deviation, color='green', marker='s', mfc='red',
         mec='green', ms=6, mew=4, capsize= 5)
plt.grid()
plt.legend()
plt.savefig("Muon Lifetime Measurement")
print('error in the system(Statistical) is approximately %{}'.format(error))

"""
Activity formula and differe
"""
plt.figure(2) # second figure 
plt.plot(rem,mu_rem, label = u"Muon Count vs Microseconds (\u03bcs)", color= 'navy', alpha = 0.75)
plt.plot(time_fit,decay_func_fit, label = "Decay Fit", color= 'orange', alpha= 0.75, ls= '--')
plt.axvline(x= log_r, label= u"Mean lifetime experimental(log-scale) {} \u03bcs".format(log_r) ,color= 'red', ls = '--')
plt.axvline(x= real_muon_lifetime, label= u"Mean lifetime actual {} \u03bcs".format(real_muon_lifetime) ,color= 'purple', ls= '--')
plt.title("Muon Lifetime Measurement_log_r")
plt.xlabel(u"Microseconds (\u03bcs)")
plt.ylabel("Muon Count")
plt.errorbar(log_r, error_point_2, xerr= standard_deviation_log_r, color='green', marker='s', mfc='red',
         mec='green', ms=6, mew=4, capsize= 5)
plt.grid()
plt.legend()
plt.savefig("Muon Lifetime Measurement_log_r")
print('error in the system(log-scale activity) is approximately %{}'.format(error_log_r))

"""
Third is similar to second but with exclusion effect.
"""
plt.figure(3) # third figure 
plt.plot(rem,mu_rem, label = u"Muon Count vs Microseconds (\u03bcs)", color= 'navy', alpha = 0.75)
plt.plot(time_fit,decay_func_fit, label = "Decay Fit", color= 'orange', alpha= 0.75, ls= '--')
plt.axvline(x= excluded_log_r, label= u"Mean lifetime experimental(log-scale) {} \u03bcs".format(excluded_log_r) ,color= 'red', ls = '--')
plt.axvline(x= real_muon_lifetime, label= u"Mean lifetime actual {} \u03bcs".format(real_muon_lifetime) ,color= 'purple', ls= '--')
plt.title("Muon Lifetime Measurement_log_r_after_correction")
plt.xlabel(u"Microseconds (\u03bcs)")
plt.ylabel("Muon Count")
plt.errorbar(excluded_log_r, error_point_3, xerr= standard_deviation_excluded_log_r, color='green', marker='s', mfc='red',
         mec='green', ms=6, mew=4, capsize= 5)
plt.grid()
plt.legend()
plt.savefig("Muon Lifetime Measurement_log_r_after_correction")
print('error in the system(log-scale activity corrected) is approximately %{}'.format(error_ex_log_r))

"""
if len(pre_mean) == len(pre_length):        #To check if mean and length len is equal.
	print('dance')   

#from uncertainties import ufloat can be used for uncertainty
	
"""
#print(time_count[len(time_count)-1]) # to understand the len concept.
#print(time)

#filter error in 0.0 - 0.2 and 0.2-0.4
#print(count)




"""
There is an error due to first third count in the system it rise from 132-80 to 80-135
which shouldn't happen normally and will be discussed in the report and presentation.

One can make the measurement better by using sample of random generated means 
and find an average value of those random systems, but I didn't want to change
the randomness and wanted to show the effect of the randomness in the data.
"""