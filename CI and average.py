import csv
from math import *

phys =  open('houses.csv', 'r')
reader = csv.reader(phys)

grouped_selling_m2 = []
selling_prices = []
pre_m2 = []

z = 1.96 #for 95% confidence interval for two tail test.

mean_while_using_selling_prices = 0
mean_while_using_selling_prices_house_size = 0

pre_variance_for_selling_prices = 0
pre_variance_for_selling_prices_house_size = 0

standard_dev_for_selling_prices = 0
standard_dev_for_selling_prices_house_size = 0

for row in reader:
	grouped_selling_m2.append(row)

for i in range(1,len(grouped_selling_m2)):
	selling_prices.append(grouped_selling_m2[i][0])

for i1 in range(1,len(grouped_selling_m2)):
	pre_m2.append(grouped_selling_m2[i1][1])

pre_two_intervals = "".join(pre_m2)
m2 = pre_two_intervals.split()

"""print(m2)
print(grouped_selling_m2)
print(selling_prices)"""

for i in range(len(selling_prices)):
	mean_while_using_selling_prices += float(selling_prices[i])
	mean_while_using_selling_prices_house_size += float(selling_prices[i]) / float(m2[i])

mean_while_using_selling_prices = mean_while_using_selling_prices/len(selling_prices)
mean_while_using_selling_prices_house_size = mean_while_using_selling_prices_house_size/len(m2)

for i in range(len(selling_prices)):
	pre_variance_for_selling_prices += (float(selling_prices[i]) - mean_while_using_selling_prices)**2
	pre_variance_for_selling_prices_house_size += (float(selling_prices[i]) / float(m2[i]) - mean_while_using_selling_prices_house_size)**2

standard_dev_for_selling_prices = sqrt(pre_variance_for_selling_prices/len(selling_prices))
standard_dev_for_selling_prices_house_size = sqrt(pre_variance_for_selling_prices_house_size/len(selling_prices))

confidence_interval_selling_prices = (mean_while_using_selling_prices-(z*standard_dev_for_selling_prices/sqrt(len(selling_prices))),mean_while_using_selling_prices+(z*standard_dev_for_selling_prices/sqrt(len(selling_prices))))
confidence_interval_selling_prices_house_size = (mean_while_using_selling_prices_house_size-(z*standard_dev_for_selling_prices_house_size/sqrt(len(selling_prices))),mean_while_using_selling_prices_house_size+(z*standard_dev_for_selling_prices_house_size/sqrt(len(selling_prices))))

print("Average selling price for houses (in thousand TL) is ", mean_while_using_selling_prices)
print("Average selling price for houses (in thousand TL)/house size (in m^2) is ", mean_while_using_selling_prices_house_size)
print("95 percent confidence interval for house prices (in thousand TL) is ", confidence_interval_selling_prices)
print("95 percent confidence interval for house prices (in thousand TL)/house size (in m^2) is ", confidence_interval_selling_prices_house_size)
print("This is only usable in the interval of minimum - maximum house size (in m^2) of the given data.")