import random
import time
import timeit

class RBT:

    class Tree():
        def __init__(self, key=0,color='RED'):
            self.right = 0
            self.left = 0
            self.p = 0
            self.key = key
            self.color = color

    def __init__(self):
        self.zero = self.Tree(key = 0, color='BLACK')
        self.root = self.zero
        self.size = 0
        self.ordered = []
        pass

    def RR(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.zero:
            y.right.p = x
        y.p = x.p
        if x.p == self.zero:
            self.root = y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y

    def LL(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.zero:
            y.left.p = x
        y.p = x.p
        if x.p == self.zero:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def maketree(self, z):
        new_node = self.Tree(key = z)
        self._maketree(new_node)
        self.size += 1

    def _maketree(self, z):
        y = self.zero
        x = self.root
        while x != self.zero:
            y = x
            if z.key < x.key :
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == self.zero:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.zero
        z.right = self.zero
        z.color = "RED"
        self.balance(z)

    def balance(self, z):
        i = 0
        while z.p.color == "RED":
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color == "RED":
                    z.p.color = "BLACK"
                    y.color = "BLACK"
                    z.p.p.color = "RED"
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self.LL(z)
                    z.p.color = "BLACK"
                    z.p.p.color = "RED"
                    self.RR(z.p.p)
            else:
                y = z.p.p.left
                if y.color == "RED":
                    z.p.color = "BLACK"
                    y.color = "BLACK"
                    z.p.p.color = "RED"
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self.RR(z)
                    z.p.color = "BLACK"
                    z.p.p.color = "RED"
                    self.LL(z.p.p)
            i += 1
        self.root.color = "BLACK"

    
    def rbsearch(self, x):
        return self.rbsearchhelp(self.root, x)

    def rbsearchhelp(self, current_node, target):
        if current_node == self.zero:
            print(str(target) + " Not Found")
        elif target == current_node.key:
            print(str(target) + " Found")
        elif target < current_node.key:
            return self.rbsearchhelp(current_node.left, target)
        else:
            return self.rbsearchhelp(current_node.right, target)

    #def Preorder(self):
        #print(self.root,'(',self.color,')', end = "  ")
        #Preorder(self.left)
        #Preorder(self.right)

    """def Postorder(root):
        Postorder(root.left)
        Postorder(root.right)
        print(root.val,'(',root.color,')', end = "  ")"""    

def main():
    rbt = RBT()
    root = 0
    no_of_elements = input("Number of elements in array ");
    no_of_elements = int(no_of_elements)
    randomizedarr = []
    for y in range(1, no_of_elements+1):
        randomizedarr.append(y)
    random.shuffle(randomizedarr)
    n = len(randomizedarr)
    print(randomizedarr)
    print(n)
    for i in range(0, n):
        root = rbt.maketree(randomizedarr[i])
    key = input("Enter key to be searched ");
    key = int(key)
    start = time.time()
    rbt.rbsearch(key)
    end = time.time()
    #print(rbt.Preorder())
    #print(rbt.Postorder())
    #print(search)
    print("Time Taken = ", end - start)
    pass


if __name__ == '__main__':
    main()