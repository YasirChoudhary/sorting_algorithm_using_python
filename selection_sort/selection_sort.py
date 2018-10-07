list_of_numbers = [5,7,8,9,3]


def sort(arg):

	n = len(arg)
	for i in range(n-1):
		i_min = i
		for j in range(i+1,n):
			if arg[j] < arg[i_min]:

				arg[j],arg[i_min] = arg[i_min],arg[j]
				#temp = arg[j]
				#arg[j] = arg[i_min]
				#arg[i_min] = temp
	return arg


def main():

	print("Numbers before Sorting")
	print(list_of_numbers)

	print("\nNumbers After Sorting")
	sorted_nums = sort(list_of_numbers)
	print(sorted_nums)


main()