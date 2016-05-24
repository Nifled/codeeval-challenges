# https://www.codeeval.com/open_challenges/97/
# Find a Writer

# CHALLENGE DESCRIPTION:

# You have a set of rows with names of famous writers encoded inside. 
# Each row is divided into 2 parts by pipe char (|). The first part 
# has a writer's name. The second part is a "key" to generate a name.

# Your goal is to go through each number in the key (numbers are separated 
# by space) left-to-right. Each number represents a position in the
# 1st part of a row. This way you collect a writer's name which you 
# have to output.

test = "3Kucdq9bfCEgZGF2nwx8UpzQJyHiOm0hoaYP6ST1WM7Nks5XjrR4IltBeDLV vA| 2 26 33 55 34 50 33 61 44 28 46 32 28 30 3 50 34 61 40 7 1 31"
test = test.strip().split('| ')

result = ""
for x in test[1].split():
	result += test[0][int(x)-1]
	
print(result.strip())