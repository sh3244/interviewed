#returns products of every other item than the one at index
def get_products_of_all_ints_except_at_index(int_list):
	product_list = [1] * len(int_list)

	#keep track of product before and after index
	before_list = 1
	after_list = 1

	#pass once through list, multiplying once per side, ~2n multiplications
	for i in range (0, len(int_list)):
		product_list[i] *= before_list
		product_list[len(int_list)-i-1] *= after_list
		before_list *= int_list[i]
		after_list *= int_list[len(int_list)-i-1]

	return product_list

def highest_product_of_3(int_list):
	product = 1
	#since there's 3 numbers, only pairs of negative numbers will be considered
	highest = 1
	lowest = -1

	min_ints = [-1,-1]
	max_ints = [1,1,1]

	#update min and max lists
	for i in range (0, len(int_list)):
		if int_list[i] < max(min_ints):
			min_ints.append(int_list[i])
			min_ints.remove(max(min_ints))
		if int_list[i] > min(max_ints):
			max_ints.append(int_list[i])
			max_ints.remove(min(max_ints))

	#constant time sort (k) for easy maths
	max_ints.sort()

	if max_ints[0] * max_ints[1] > min_ints[0] * min_ints[1]:
		for i in max_ints:
			product*=i
	else:
		product=max_ints[2]*min_ints[0]*min_ints[1]

	return product

def efficient_drops(integer):
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

print efficient_runtime()

#print get_products_of_all_ints_except_at_index(int_list)

