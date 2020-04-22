import random
from decimal import *
import time
import decimal
import timeit
 
class Tree:
	def __init__(self,key): 
		self.left = 0
		self.right = 0
		self.val = key 
def insert(root,node): 
	if root == 0: 
		root = node 
	else: 
		if root.val < node.val: 
			if root.right == 0: 
				root.right = node 
			else: 
				insert(root.right, node) 
		else: 
			if root.left == 0: 
				root.left = node 
			else: 
				insert(root.left, node)  
def inorder(root): 
	if root != 0: 
		inorder(root.left) 
		print(root.val) 
		inorder(root.right) 

def preorder(root): 
	if root != 0: 
		print(root.val)
		preorder(root.left)  
		preorder(root.right) 

def postorder(root): 
	if root != 0: 
		postorder(root.left)  
		postorder(root.right)
		print(root.val) 

def BST(root, a):
        if a < root.val:
            if root.left == 0:
                print (str(a)+" Not Found")
                return
            return BST(root.left, a)
        elif a > root.val:
            if root.right == 0:
                print (str(a)+" Not Found")
                return
            return BST(root.right, a)
        else:
            print(str(a) + " is found")

no_of_elements = input("Number of elements in array ");
no_of_elements = int(no_of_elements)
randomizedarr = []
for y in range(1, no_of_elements+1):
	randomizedarr.append(y)
random.shuffle(randomizedarr)
n = len(randomizedarr)
print(randomizedarr)
print(n)
#print(key)
r = Tree(randomizedarr[0])
for i in range(1, n):
	insert(r, Tree(randomizedarr[i]))
a = input("Enter key to be searched ");
a = int(a)
start = timeit.default_timer()
BST(r, a)
end = timeit.default_timer()
print("Inorder is : ") 
inorder(r)
#end = time.time()
print("Preorder is : ")
preorder(r)
print("Postorder is : ")
postorder(r)
#end = time.time()
#d = decimal.Decimal(end-start)
#print(d)
#print(timeit.timeit(findval(r, a), number = 1))
time = end-start
print("Time Taken = ", time);
