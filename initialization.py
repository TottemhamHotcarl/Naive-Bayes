testListNumber = [1370, 326, 1897, 916, 1086, 22, 144, 119, 596, 463, 327, 579, 361, 653, 1910, 27, 1071, 1933, 716, 1363, 830, 1133, 1554, 1351, 1225, 1297, 1850, 1161, 459, 1644, 378, 1857, 963, 874, 151, 1025, 619, 1590, 1353, 18, 1634, 82, 172, 1903, 1508, 1316, 1208, 1939, 318, 1100, 1214, 404, 101, 1909, 1424, 781, 1624, 1011, 518, 1278, 334, 106, 1860, 1095, 1301, 544, 1222, 1292, 856, 323, 1403, 1213, 1546, 1659, 705, 1772, 1608, 1796, 1478, 301, 376, 297, 1465, 62, 873, 936, 1428, 755, 1400, 512, 903, 341, 967, 1343, 1227, 1475, 413, 431, 1577, 383, 65, 258, 801, 272, 564, 699, 240, 863, 797, 644, 1034, 1313, 1896, 1828, 1050, 58, 1844, 1473, 1717, 709, 1480, 1524, 216, 807, 238, 1543, 1399, 904, 115, 1840, 40, 1781, 1843, 370, 504, 550, 1511, 1529, 1439, 1186, 1711, 1542, 1657, 532, 1251, 181, 620, 283, 454, 539, 252, 994, 877, 1010, 1967, 1505, 1039, 586, 1177, 210, 1756, 168, 750, 1552, 118, 588, 1058, 1386, 492, 852, 810, 282, 1201, 865, 1995, 887, 1911, 398, 1981, 1206, 313, 45, 1387, 1662, 741, 566, 869, 1999, 592, 325, 369, 889, 1487, 1798, 362, 682, 422, 1743, 1949, 352]


path = "/files1b/1606558/Desktop/Machine Learning/Naive Bayes Question 2/movie-pang02.csv"
path2 = "/files1b/1606558/Desktop/Machine Learning/Naive Bayes Question 2/train.txt"
path3 = "/files1b/1606558/Desktop/Machine Learning/Naive Bayes Question 2/tests.txt"
train = open(path2,'w')
test = open(path3,'w')


file_object  = open(path, 'r')
b = file_object.readlines()


n = len(b)-1
print(n*90//100)

M = []
lists = []
trainList = []
testList = []


for i in range(1,n):
	if i in testListNumber:
		test.write("%s\n" % b[i])
		testList.append(b[i])

	else:
		train.write("%s\n" % b[i])
		trainList.append(b[i])
	
	t = b[i].split(",")
	q = t[1].split(" ")
	for i in q:
		if i.strip() not in lists:
			lists.append(i.strip())
			M.append([i.strip(), 1, 1])
			
	




number_of_postive = 0
number_of_negative = 0
total_unit = 0
r = 0 
for item in trainList:
	t = item.split(",")
	if t[0] == "Pos":
		index = 1
		number_of_postive = number_of_postive + 1
		total_unit = total_unit + 1
	if t[0] == "Neg":
		index = 2
		number_of_negative = number_of_negative + 1
		total_unit = total_unit + 1
	q = t[1].split(" ")
	for i in q:
		for j in range(n):
			if i.strip() == M[j][0]:
				M[j][index] = M[j][index] + 1
	print(r)
	r = r + 1

pathwrite = "/files1b/1606558/Desktop/Machine Learning/Naive Bayes Question 2/words.txt"
filewrite = open(pathwrite,'w')


with open(pathwrite, 'w') as f:
    f.write("%s\n" % [number_of_postive/total_unit,number_of_negative/total_unit])
    for item in M:
            f.write("%s\n" % item)
		
		
