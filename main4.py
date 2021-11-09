def greeting():
	return "Hello"

	# greeting() = "Hello" <-- what I returned

	fullgreeting = greeting()
	print(fullgreeting)

def add(a,b):
	return a+b

def multiply(a, b):

	return a*b
answer = add(2,3)
answer = multiply(4, answer)
print(answer)


def luckify(string):
    return string + "777"
 
print(luckify("Joey"))
luckyname = luckify("Joey")
print(luckyname) 
luckyname = luckify(luckyname)
print(luckyname)