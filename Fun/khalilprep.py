def arrayToString(arr):
	Result = ‘’
	Beginning = arr[0]
	End = arr[0]
	If len(arr) == 0 or len(arr) == 1:
		return arr
	for i, num in enumerate(arr[1:]):
		If num == End + 1:
			End = num
			if i == len(arr) - 1:
				Result += str(Beginning) + ‘-’ + str(End)
		else:
			if beginning == end:
				Result += str(Beginning) +’, ‘
			else:
				Result += str(Beginning) + ‘-’ + str(End)+ ’, ‘ 
			Beginning = num
			End = num
	return result
