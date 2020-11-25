def count_occurence(list, x): 
	count = 0
	for ele in list: 
		if (ele == x): 
			count = count + 1
	return count 
list = [8, 6, 8, 10, 8, 20, 10, 8, 8] 
x = 8
print('{} has occurred {} times'.format(x, count_occurence(list, x))) 
