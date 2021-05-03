'''
5/3/21

Review

Recursion

def Function(parameter):
	if(): # Base Condition
		return something
	else:
		return something + Function(parameter +/- 1)

# 2. Fibonacci Sequence With a Recursive Function
# NOTE: Keep Adding the Last 2 Numbers
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 45, .....
def fibonacci(n):
	if(n <= 1):
		return n
	else:
		return (fibonacci(n-1) + fibonacci(n-2))

nterm = int(input("How Many Terms? "))

if(nterm <= 0):
	print("Please Input a Positive Number.")
else:
	print("Fibonacci Sequence: ")

	for i in range(nterm):
		print(fibonacci(i))

# 3. Fibonacci Sequence With a Loop
n1, n2 = 0, 1
count = 0

nterm = int(input("How Many Terms? "))

if(nterm <= 0):
	print("Please Input a Positive Number.")
else:
	print("Fibonacci Sequence: ")

	while(count < nterm):
		print(n1)
		nth = n1 + n2

		n1 = n2
		n2 = nth
		count += 1


Access Values in Strings
- To access substrings, Use the square brackets for slicing along with the index or indicies to obtain your substring.

var = "Hello"

# Individual
string:     |  H  |  e  |  l  |  l  |  o  |
positive:   |  0  |  1  |  2  |  3  |  4  |
negative:   |  -5 |  -4 |  -3 |  -2 |  -1 |

# Consective
string:     |  H  |  e  |  l  |  l  |  o  |
index:      0     1     2     3     4     5

In case of printing consective characters, it needs to start beginning index and colon, then ending index.

ex) print "ello" from var
print(var[1: ])

List1 = ["a","b","g","y","j","k","h"]
print(List1[2:4])

String = "Students"
print(String[:5])
print(String[5:])
'''

var1 = "Hello World!"
var2 = "Python Programming"

# 1. Print "h" from var2
print(var2[3])
print(var2[-15])
# 2. Print "hi" from var1 and var2
print(var1[0] + (var2[15]))
print(var1[0] + (var2[-3]))
print(var2[3] + (var2[15]))