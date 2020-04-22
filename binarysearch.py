import random
import timeit
def binarysearch (randomizedarr, low, high, key): 
    if low <= high: 
        mid = int((low + high) // 2)
        if randomizedarr[mid] == key: 
            return mid 
        elif randomizedarr[mid] > key: 
            return binarysearch(randomizedarr, low, mid-1, key) 
        else: 
            return binarysearch(randomizedarr, mid + 1, high, key) 
    else: 
        return -1

no_of_elements = input("Number of elements in array ");
no_of_elements = int(no_of_elements)
randomizedarr = []
for y in range(1, no_of_elements+1):
	randomizedarr.append(y)
random.shuffle(randomizedarr)
#print("Generated Array",randomizedarr);
randomizedarr.sort()
n = len(randomizedarr)
print("Sorted Array", randomizedarr)
print(n)
key = input("Enter key to be searched ");
key = int(key)
start = timeit.default_timer()
search = binarysearch(randomizedarr,0, n-1, key)
end = timeit.default_timer()
print(search)
if(search == -1):
	print("Number not found")
else:
	print("Number found at ", search)
print("Time Taken = ", end-start);
