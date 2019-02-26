import numpy as np

path = "/files1b/1606558/Desktop/Machine Learning/Naive Bayes/whole_data.txt"

file_object  = open(path, 'r')
b = file_object.readline()
lists = []
while b != "":
	t = b.split(" ")
	for i in t:
		if i.strip() not in lists:
			lists.append(i.strip())
	
	b = file_object.readline()

print(lists)
n = len(lists)
print(n)

M = []

for i in range(n):
	M.append([lists[i], 1, 1])
print(M)


path2 = "/files1b/1606558/Desktop/Machine Learning/Naive Bayes/reviews.txt"

file_object2  = open(path2, 'r')
b = file_object2.readline()
number_of_postive = 0
number_of_negative = 0
total_unit = 0

while b != "":
	print("pizza")
	t = b.split(" ")
	if t[0] == "1":
		index = 1
		number_of_postive = number_of_postive + 1
		total_unit = total_unit + 1
	if t[0] == "-1":
		index = 2
		number_of_negative = number_of_negative + 1
		total_unit = total_unit + 1

	for i in t:
		for j in range(n):
			
			if i == M[j][0]:
				M[j][index] = M[j][index] + 1
		print(M)

	b = file_object2.readline()
print("pizza")
print(number_of_postive/total_unit, number_of_negative/total_unit)
table = M

pathwrite = "/files1b/1606558/Desktop/Machine Learning/Naive Bayes/prob.txt"
filewrite = open(pathwrite,'w')

for i in range(n):
	total = M[i][1] + M[i][2]
	print(total)
	u = [1,2]
	for t in u:
		table[i][t] = table[i][t]/total
with open(pathwrite, 'w') as f:
    f.write("%s\n" % [number_of_postive/total_unit,number_of_negative/total_unit])
    for item in table:
        if item[0] != "1" and item[0] != "-1":
            f.write("%s\n" % item)
print(table)


	

