from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")


def sort(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with merge sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	if len(container) <=1:
		return container
	else:
		middle =len(container) // 2
		print ('-------------------------')
		print('Commit split')
		print('left container:',container[:middle])
		print('right container:', container[middle:])
		print('Split left contfiner:')
		left_container = sort(container [:middle])
		print('Split left contfiner:')
		right_container = sort(container[middle:])

	print('merge',left_container,right_container)
	return merge(left_container ,right_container)
def merge(left_container ,right_container):
	sorted_ = []
	left_container_index = 0
	right_container_index = 0

	left_container_length = len(left_container)
	right_container_length = len(right_container)

	for _ in range(left_container_length + right_container_length):
		if (left_container_index < left_container_index) and (right_container_index < right_container_length):
			if left_container[left_container_index ]<= right_container[right]:
				sorted_.append(left_container[left_container_index])
				left_container_index +=1
			else:
				sorted_.append(right_container[right_container_index])
				right_container_index +=1

		elif left_container_index == left_container_length:
			sorted_.append(right_container[right_container_index])
			right_container_index +=1
		elif right_container_index == right_container_length:
			sorted_.append(left_container_length)
			left_container_index += 1
	print("Merged:",sorted_)
	return sorted_


if __name__ == "__main__":
	list = [6,5,12,10,9,1]
	print(list)
	print(sort(list))