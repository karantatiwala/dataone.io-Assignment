
# coding: utf-8
#!/usr/local/bin/python
# coding: latin-1
import csv
import sys
import os
 
f = open(sys.argv[1], "r")
reader = csv.reader(f)

count = 0
for row in reader:
	count = count + 1

# print count
f.close()


f = open(sys.argv[1], "r")
reader1 = csv.reader(f)

# print len(sys.argv)-2

# print sys.argv[4]


ShopsPro = [None] * (len(sys.argv)-2)

for shop in range(len(sys.argv)-2):
	ShopsPro[shop] = [None] * count

Sum = [0] * count



for line in reader1:
	for i in range(2, (len(sys.argv))):
		if sys.argv[i] in line:
			ShopsPro[i-2][int(line[0])] = float(line[1])


# print ShopsPro

for i in range(len(sys.argv)-2):
	for j in range(count):

		# print j, Sum[j], ShopsPro[i][j]
		if Sum[j] != 0 and ShopsPro[i][j] == None:
			print "none"
			exit()
			# print Sum[j]
			# print ShopsPro[i][j]
		
		else:
			if ShopsPro[i][j] != None:
				Sum[j] +=  ShopsPro[i][j]
				# print Sum[j]
				# print ShopsPro[i][j]
		
		

# print Sum

for k in Sum:
	if k != 0:
		minimum = k

for k in Sum:
	if k != 0 and k < minimum:
		minimum = k

print Sum.index(minimum), minimum
f.close()



