from collections import deque

input_string = "{a+(b*c+[d*e/{f^g}]/22}"
opening_list = list("({[")
closing_list = list(")}]")

d = deque(maxlen = len(input_string))

input_string_filter = filter(lambda x:x in list("({[]})"), input_string)
k = 0
for i in input_string:
	if i in opening_list:
		d.append(i)

	elif i in closing_list:
		
		if opening_list.index(d[-1]) == closing_list.index(i):
			d.pop()
		else:
			print "unbalanced paranthesis at position"
			print k+1
			break
	else:
		pass

	if (len(d)==0 and i==input_string[-1]):
		print "balanced test case"
		break
	
	k+=1

	#print "balanced test case"

