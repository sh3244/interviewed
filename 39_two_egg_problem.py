#this method maintains a worst case runtime of 14 where n=100 (the quadratic root is actually 13.651)
#this method is technically the best worst case runtime for n=105
#average cases may be better with other techniques
#where n=100, the average runtime is 9.35 for even input

def efficient_drops(integer):
	#skip is the intial skip, decreasing by one for consistent worst case runtime(max 14 test drops)
	skip = 14
	current = skip
	count = 1

	while current != integer:
		if current > integer:
			count += skip-(current-integer)
			current = integer
		else:
			skip-=1
			current+=skip
			count+=1

	print current
	print count
	print "\n"
	#print count
	return count


def efficient_runtime():
	totaltime = 0

	for floor in range(1,100):
		totaltime += efficient_drops(floor)

	return totaltime

#prints average runtime of using lowest worst case algorithm for finding the exact floor an egg breaks
print efficient_runtime()