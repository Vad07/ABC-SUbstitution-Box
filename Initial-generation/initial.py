#intial substitution box

#using choatic function

#major rebooted
import test
import math 
import random
from random import randint


def is_bijective(s):
    """ Checks if the s box is bijective """
    for i in range(len(s)):
        if i not in s:
            print(i)
            return False
    return True

lower_limit = 0

count = 0

upper_limit = 255

empty_array = []

z = 3.99

flag = 1

i = 0

# for i in range(255):

# 	empty_array.append(0);

x = random.randint(lower_limit,upper_limit)

y = random.uniform(0,1)

print 'intial y'

print y

while flag:


	if count > 255:
		break

	y = z*y*(1-y)

	y = random.uniform(0,1)


	print 'final y'

	print count

	temp = int(y*10**5) % 256

	# temp = temp % 256

	# temp = math.floor(temp)

	#temp = int(temp)
	
	# print 'temp is'

	# print temp


	if temp not in empty_array:

		empty_array.append(temp)

		count = count + 1


# for i in range(256):

# 	empty_array[i] = int(math.floor(empty_array[i]))


# for i in range(256):

# 	count =  empty_array.count[i]

# 	for j in range(i):


length = len(empty_array)

# print length
print empty_array

print is_bijective(empty_array)



print test.value_nonl(empty_array)


#print('the random number is',x)

#x=81;
	
# for iterate in range(user_iter):

# 	t = theta[node] + nutrientsfunc(theta,flag,node,last);
		
# 	f = theta[node+x] + nutrientsfunc(theta,flag,node+x,last);
		
# 	diffrence = f - t;

# 	# iterate = iterate + 1;

# 	if diffrence > threshold: 

# 		temp = theta[node];

# 		theta[node] = theta[node+4];

# 		theta[node+4] = temp;

# 		node = node + 4;

# 		flag1 = 1;

# 		if node > 251:

# 			break;

	# if S2 > S1:

	# 	break;
	
	# else:

	# 	miss = miss + 1;

# print flag1

# print theta
			
