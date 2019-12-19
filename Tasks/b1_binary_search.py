
from typing import Any, Sequence, Optional



def binary_search(elem: Any, arr: Sequence) -> Optional[int]:
	"""
	Performs binary search of given element inside of array

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""
	left = -1
	right = len(arr)
	while right > left + 1:
		middle = (left + right) // 2
		if arr[middle] > elem:
			right = middle

		else:
			left = middle
		elif:
		 if middle == ele


	return


	# print(elem, arr)


