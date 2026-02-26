'''
Write a Python function to print 1 to n using recursion.
'''

def count(n,a):
    if(a==n):
        print(a)
        return
    else:
        print(a)
        return count(n,a+1)
    
count(10,1)