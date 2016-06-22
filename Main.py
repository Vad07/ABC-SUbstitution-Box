import math 
import test
import random
from random import randint
import numpy


theta = [86, 45, 170, 67, 130, 238, 59, 189, 194, 100, 57, 188, 8, 49, 47, 48, 44, 106, 125, 38, 54, 197, 56, 227, 190, 180, 165, 168, 193, 179, 219, 58, 205, 214, 120, 181, 171, 97, 251, 196, 90, 117, 96, 143, 32, 127, 113, 62, 155, 249, 123, 64, 69, 208, 80, 131, 245, 246, 228, 242, 241, 23, 200, 151, 210, 122, 9, 60, 140, 225, 132, 183, 104, 70, 20, 147, 133, 34, 65, 91, 105, 43, 215, 138, 203, 164, 137, 217, 110, 250, 89, 243, 19, 95, 2, 169, 4, 185, 177, 7, 46, 176, 129, 0, 6, 81, 166, 128, 119, 209, 121, 134, 27, 18, 142, 244, 61, 224, 31, 221, 144, 52, 232, 108, 93, 234, 158, 103, 201, 41, 135, 191, 85, 25, 39, 202, 248, 167, 35, 17, 68, 182, 152, 223, 98, 55, 16, 40, 187, 99, 204, 75, 124, 107, 175, 229, 42, 36, 14, 33, 29, 220, 239, 247, 10, 30, 5, 11, 237, 94, 15, 213, 77, 21, 141, 1, 82, 207, 235, 28, 233, 83, 254, 150, 153, 162, 63, 159, 172, 198, 71, 118, 146, 13, 111, 51, 174, 161, 72, 206, 230, 178, 192, 226, 252, 157, 12, 212, 253, 199, 114, 92, 184, 186, 66, 160, 76, 148, 218, 240, 101, 173, 139, 79, 74, 73, 216, 222, 24, 109, 149, 84, 126, 112, 87, 88, 255, 154, 37, 211, 78, 115, 102, 156, 145, 136, 3, 231, 163, 53, 116, 236, 26, 50, 22, 195]
S_array = []

p_array = []

flag = 0

first = 0

last = 255

x  = random.randint(0,255)

y = random.randint(0,127)


def calc_objectivefn_value(theta,node,x,flag):

	func = 0

	if flag ==0:

		flag = 1

		func = S_array[node] + y*(S_array[node]-x)

		# func  = func % 255

		if func > 0:

			# func = 1/(1+func)


			func = int(func*10**5) % 256
		
		else:

			func = int(1+abs(func))
			
			func = func %256




	else:

		flag =1 

	return func

def probabilityfunc(p_array,flag,S_array,length):

	p_tot = sum(S_array)

	# print p_tot



	temp2 = 0

	# print length

	for iterate in range(0,length):

		# print iterate

		if iterate >= length:
			break;

		
		lele = float(((S_array[iterate]*12345.12345/p_tot)%1));

		# print lele

		p_array.append(float(((S_array[iterate]*12345.12345/p_tot)%1)));

		temp2 = temp2 + 1;


	return p_array	


desired_solution = input('Enter the number of desired solutions wanted not greater than 255')

print desired_solution

# z = random.randint(desired_solution+1,255)

t = 0

for t in range(0,desired_solution):

	x = random.randint(first,last)

	if x != 128:

		S_array.append(x);

# lol = calc_objectivefn_value(S_array,desired_solution-3,12,flag)

# print lol

length = len(S_array)

# print S_array
# print length


temp = 0

i = 0

probabilityfunc(p_array,flag,S_array,length);


# print p_array

for iterate in range(desired_solution):

	x = random.randint(0,desired_solution)

	lol = calc_objectivefn_value(S_array,x-1,12,flag)


	# if (temp!=z)
	temp3 = iterate + 1
	
	if temp3 >= desired_solution:
		break

	
	if p_array[i] > p_array[temp3]:

		flag = 3

		if S_array[iterate] - lol < S_array[temp3]:

			temp = theta[S_array[temp3]];

			theta[S_array[temp3]] = theta[S_array[i]];

			theta[S_array[iterate]] = temp;

			flag = 2

	i = i+1


print theta

print flag

print test.value_nonl(theta)

# print temp







