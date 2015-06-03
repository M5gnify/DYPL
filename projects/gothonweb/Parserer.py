def parse(str):
	string_to_return =""
	indentation_level = 0
	for c in str:
		if c == "{" or c == "[":
			indentation_level += 1
			string_to_return += c+"\n"+indentation(indentation_level)
		elif c == ",":
			string_to_return += ",\n"+indentation(indentation_level)
		elif c == "}" or c == "]":
			indentation_level -= 1
			string_to_return += "\n"+indentation(indentation_level)+c
		else:
			string_to_return += c
		
	return string_to_return

def indentation(var):
	str = ""
	for i in range(var):
		str += "\t"
	return str
