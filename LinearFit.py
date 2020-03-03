"""
Successfully fits when error bars in middle range sufficently large to just encompas a min and max gradients form the extremal points
Self correction currently does not work properly
TODO: Fix self correction
"""

#Data format is {x:[y,error in y]}

data = {
12:[0.183,0.007],
10:[0.152,0.012],
6:[0.094,0.004],
4:[0.062,0.004],
2:[0.0298,0.0018],
8:[0.122,0.007],
14:[0.214,0.005]}

x = sorted(list(data.keys()))

satisfied = False
n=0
m=0
while(satisfied==False):
	min_min = data[x[n]][0]-data[x[0]][1]
	max_max = data[x[-(1+m)]][0]+data[x[-1]][1]

	max_grad = (max_max-min_min)/(x[-(1+m)]-x[n])

	max_min = data[x[0]][0]+data[x[0]][1]
	min_max = data[x[-1]][0]-data[x[-1]][1]

	min_grad = (min_max-max_min)/(x[-(1+m)]-x[n])

	average_grad = (min_grad+max_grad)/2

	min_fits = []
	max_fits = []

	for i in x:
		min_y = max_min+min_grad*(i-x[n])
		max_y = min_min+max_grad*(i-x[n])

		if(min_y>=(data[i][0]-data[i][1])):
			min_fits.append(True)
		else:
			min_fits.append(False)
			print("Min doesn't fit for ",i)

		if(min_y<=(data[i][0]+data[i][1])):
			max_fits.append(True)
		else:
			max_fits.append(False)
			print("Max doesn't fit for ",i)

	min_satisfied = True
	max_satisfied = True
	for i in min_fits:
		if i == False:
			min_satisfied = False

	for i in max_fits:
		if i == False:
			max_satisfied = False

	if(min_satisfied==True):
		if(max_satisfied==True):
			satisfied = True
			print("Minimum gradient = ",min_grad)
			print("Maximum gradient = ",max_grad)
			print("Average gradient = ",average_grad)
		else:
			print("Max too steep")
			print("Minimum gradient = ",min_grad)
			print("Maximum gradient = ",max_grad)
			print("Average gradient = ",average_grad)
	else:
		print("Min too shallow")
		print("Minimum gradient = ",min_grad)
		print("Maximum gradient = ",max_grad)
		print("Average gradient = ",average_grad)

	if(satisfied == False):
		if(n>m):
			m+=1
		else:
			n+=1
