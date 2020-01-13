import typing

_Tt = typing.TypeVar("_Tt")


def sort(container: typing.Collection[_Tt]) -> typing.Collection[_Tt]:
	"""
	Sort input container with bubble sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	container
	replace = 0
	for i in range (len(container)-1):
		for j in range(len(container)-1 -i):
			if container[j] > container[j + 1]:
				container[j], container[j + 1] = container[j + 1] + container[j]
				replace += 1
		print('count replase',replace)
		replace = 0
	return container
if __name__ == "__main__":
	import random
	N = 5
	# shuffle_list = list(range(N))
	shuffle_list =[4,1,2,3,0]
	# random.shuffle(shuffle_list)
	print(sort(shuffle_list))