nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]

def flat_generator(n_list):
	for element in n_list:
		for any_element in element:
			yield any_element





print (nested_list)
new_list = []
for item in  flat_generator(nested_list):
	new_list.append(item)

print(new_list)

	#['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]