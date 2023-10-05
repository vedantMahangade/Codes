'''
Problem Statement:
What is the time complexity of this algorithm, in terms of n?
    for (int i = 1 to n) {
        j = i
        while (j < n) {
            k = j
            while (k < n) {
                Sum += a[i]*b[j]*c[k]
                k += log log n
            }
            j += log (j+10)
        }
    }
'''
import math
import time
import random

#pseudo code in the option 4 implemented as a python program
def algorithm(n, a, b, c):
    Sum = 0
    start_time = time.time()
    for i in range(1,n):
        j=i
        while j < n:
            k=j
            while k < n:
                Sum = Sum + a[i] * b[round(j)] * c[round(k)] #j and k needs to be rounded off as decimal cant be used as list index
                k = k + math.log2(math.log2(n))
            j = j + math.log2(j+10)
    print(n,"\t\t",time.time() - start_time)    # this line prints the execution time of each loop
    return Sum


#inputs to get 3 values which will be used to execute the pseudo code implementation
# with different values of n ranging from n_start to n_end with an increment of n_inc
n_start = int(input("Enter the starting value for n:"))
n_end = int(input("Enter the last value for n:"))
n_inc =int(input("Enter the increment value:"))

#lists a, b and c are defined with random 100000 integers
a = [random.randint(5,75) for _ in range(100000)]
b = [random.randint(75,125) for _ in range(100000)]
c = [random.randint(125,200) for _ in range(100000)]

print(" n\t\tExecution Time")
print("------\t\t------------------------")

# the below loop will run the pseudo code implementation for different values of n 
# ranging from n_start to n_end with an increment of n_inc
n=1000
while n<=5000:
    result = algorithm(n, a, b, c)
    n = n + 100



