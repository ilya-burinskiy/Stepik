s = input() 
stack = []

left_braces = ['[', '(', '{']
right_braces = [']', ')', '}']
braces = list(zip(left_braces, right_braces))

for i, sym in enumerate(s, start=1):

	if sym in left_braces:
		stack.append((sym, i))

	elif sym in right_braces:
		if len(stack) != 0:
			top = stack.pop()
			brace = top[0]
			if not ((brace, sym) in braces):
				stack.append((sym, i))
				break

		else:
			stack.append((sym, i))
			break

	else:
		continue

if len(stack) != 0:
	print(stack.pop()[1])
else:
	print('Success')