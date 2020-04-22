import random
import timeit
import time
def linearsearch(randomizedarr, n, key):
	for i in range(0, n):
		if(randomizedarr[i] == key):
			return i;
	return -1;

no_of_elements = input("Number of elements in array ");
no_of_elements = int(no_of_elements)
randomizedarr = []
for y in range(1, no_of_elements+1):
	randomizedarr.append(y)
random.shuffle(randomizedarr)
n = len(randomizedarr)
print(randomizedarr)
print(n)
key = input("Enter key to be searched ");
key = int(key)
start = timeit.default_timer()
search = linearsearch(randomizedarr, n, key)
end = timeit.default_timer()
if(search == -1):
	print("Number not found")
else:
	print("Number found at ", search);
print("Time Taken = ", end-start);


