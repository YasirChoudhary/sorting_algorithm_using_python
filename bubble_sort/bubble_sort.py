list_of_numbers = [8,7,56,14,1]

def sort(arg):

	n = len(arg)
	for k in range(n-1):
		for i in range(n-1-k):
			if arg[i] > arg[i+1]:
				arg[i],arg[i+1] = arg[i+1],arg[i]
	return arg


def main():

	print("Numbers before Sorting")
	print(list_of_numbers)

	print("\nNumbers after Sorting")
	sorted_nums = sort(list_of_numbers)
	print(sorted_nums)


main()