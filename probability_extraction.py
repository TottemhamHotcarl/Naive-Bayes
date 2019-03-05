import math

def log(x,n):
	print(math.log10(x))
	return math.log10(x)

path = "/files1b/1606558/Desktop/Machine Learning/Naive Bayes Question 2/number.txt"
path2 = "/files1b/1606558/Desktop/Machine Learning/Naive Bayes Question 2/probs.txt"
file_object  = open(path, 'r')
tabler = open(path2, 'w')
b = file_object.readline()
probability = b
b = file_object.readline()
M = []
while b != "":
	x = b[2:-2]
	#print(x)
	#print(x.split(","))
	v = x.split(",")
	#print(v[0][:-1])
	string = v[0][:-1]
	#print(int(v[1]))
	posV = int(v[1])
	negV = int(v[2])
	total = posV + negV
	
	M.append([string,posV/total,negV/total])
	b = file_object.readline()

	
with open(path2, 'w') as f:
    f.write("%s\n" % probability)
    for item in M:
        f.write("%s\n" % item)	
table = M



#______________________________________________________________________-
review = input()


pxgivenpos = 1
pxgivenneg = 1

u = [1,2]
n = len(table)

for i in range(n):
	#print("pizza")
	#print(table[i][0],table[i][1], review)
	if table[i][0] in review:
		pxgivenpos = pxgivenpos*table[i][1]
	elif table[i][0] not in review:
		wee = (1 - table[i][1])
		
		pxgivenpos = pxgivenpos*(wee)
	if (pxgivenpos) > 0:
		print(pxgivenpos)
for i in range(n):
	#print("pizza")
	#print(table[i][0],table[i][2], review)
	if table[i][0] in review:
		pxgivenneg = math.log10(pxgivenneg) + math (table[i][2])
	elif table[i][0] not in review:
		pxgivenneg = (pxgivenneg)*(1 - table[i][2])


temp = probability[1:-2].split(",")

print(pxgivenpos)
print(pxgivenneg)
prob_of_post = float(temp[0])
prob_of_neg = float(temp[1])
probability_of_x = log((prob_of_post),10) + pxgivenpos + log((prob_of_neg),10) + pxgivenneg




#% positive

prob_of_review_positive = (pxgivenpos + log(prob_of_post,10)) - log(probability_of_x,10)
prob_of_review_negative = (pxgivenneg + log(prob_of_neg,10)) - log(probability_of_x,10)

print("The probability of this review being positive is:", prob_of_review_positive)
print("The probability of this review being negative is:", prob_of_review_negative)
