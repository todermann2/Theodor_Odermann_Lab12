def Mean(numbers):
	if not numbers:
		return None
	return sum(numbers) / len(numbers)
	
def Median(numbers):
	if not numbers:
		return None
		
	sorted_numbers = sorted(numbers)
	new = len(sorted_numbers)
	middle = new // 2
	
	if new % 2 == 0:
		return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
	else:
		return sorted_numbers[middle]
