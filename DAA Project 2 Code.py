'''
Problem Statement: Convex hull
We are given a set P of n points in a two-dimensional plan, and we want to compute the convex hull of P. 
The convex hull is defined as the smallest convex polygon containing the points. (A way to visualize a 
convex hull is to imagine nails on all the points of the plane and put an elastic band around the points 
– the shape of the elastic band is the convex hull.) 

Describe an O(n log n) time divide and conquer algorithm to find the convex hull of the set P of n points.
'''

import random
import time

# list to store input pointspoint_range


# List to store edges of Convex Hull that is computed
convexHullEdge = []

# Function defined to get what side does the point P lie with respect to line LR
def whichSide(L, R, P):
    # getting x and y coordinates of 3 points
    x1, y1 = L
    x2, y2 = R
    x3, y3 = P

    # Consider 2 lines LP and LR, 
    # LP can be shown as vector (x3-x1)i + (y3-y1)j
    # LR can be shown as vector (x2-x1)i + (y2-y1)j
    # By finding the Cross products of these two vectors we can find if they are Clockwise(right) or Anticlock wise(left)
    # | x3-x1   y3-y1 |
    # | x2-x1   y2-y1 |
    cross_product = (x3-x1)*(y2-y1)-(x2-x1)*(y3-y1)

    if cross_product < 0:
        return 'right'
    elif cross_product > 0:
        return 'left'
    else:
        return 'onLine'
    

def ConvexHull(L, R, partition):
    # if there are no points in the partition then return
    if len(partition) == 0:
        return
    
    #Calculating the point which lies at the maximum distance from line LR
    x1, y1 = L
    x2, y2 = R
    a = y2 - y1
    b = x1 - x2
    c = x2*y1 - x1*y2
    maximumDistance = -1
    F = None

    for point in partition:
        x, y = point
        distance = abs(a*x + b*y + c)
        if distance>maximumDistance:
            distance = maximumDistance
            F = point
    x, y = F

    # Since two new edges are discovered, we remove the previous edge and add the two new ones
    convexHullEdge.remove((L, R))
    convexHullEdge.append((L, F))
    convexHullEdge.append((F, R))

    # Dividing the partition into sub partitions
    # we check if the point lies on right of LF or on right of FR. 
    # if the point lies within the triangle LFR, then we discard those points
    partition.remove(F)
    LF_Right = []
    FR_Right = []
    for point in partition:
        if whichSide(L, F, point) =='right':
            LF_Right.append(point)

        if whichSide(F, R, point) == 'right':
            FR_Right.append(point)

    # Divide and Conquer logic
    # the set of points is divided and recursivly called two times
    ConvexHull(L, F, LF_Right)
    ConvexHull(F, R, FR_Right)

def preProcess(points):
    # sorts the points based on x-coordinate(k[0]) and then by the y-coordinate(k[1])
    sortedPoints = sorted(points, key = lambda c: [c[0], c[1]])   

    # get the leftmost and rightmost points L and R
    L = sortedPoints[0]
    R = sortedPoints[-1]

    # Dividing the set of points on the Left and right sides of Line LR
    LR_Right = []
    LR_Left = []
    for point in sortedPoints:
        leftOrRight = whichSide(L, R, point)
        if leftOrRight == 'right':
            LR_Right.append(point)
        elif leftOrRight == 'left':
            LR_Left.append(point)
        else:
            pass
    
    convexHullEdge.append((L,R))
    convexHullEdge.append((R,L))



    # Divide and Conquer logic
    # the set of points is divided in half and recursivly called two times
    ConvexHull(L, R, LR_Right)
    ConvexHull(R, L, LR_Left)



############ Driver Code for execution time calculation ################
if __name__ == '__main__':

    # point_range is the range of the coordinates i.e. the x and y values can go from -5 to 5
    point_range = 5

    # n is the input length that will determine the execution time
    # Creating a while loop which will execute the entire code for different values of n and compute the execution time
    n = 5
    print()
    while n <= 10:
        points = []
        #the loop below stores n random coordinates in the points list.
        for i in range(0, n):
            points.append([random.randint(-1,7), random.randint(-1,7)])

        print("\n------------------------------------------------------------------------------")
        print("Computing Convex Hull for Set P of {} points".format(n))
        print("\nSet P: ", points)

        start_time = time.time()
        preProcess(points)
        execution_time = time.time() - start_time

        # Extracting distinct set of coordinates for printing from list of edges
        convexHullPoints = []
        for edge in convexHullEdge:
            for point in edge:
                if point not in convexHullPoints:
                    convexHullPoints.append(point)

        
        print("\nComputed Convex Hull of Length {} is:\n{}".format(len(convexHullPoints), convexHullPoints))
        print("\nTime taken for {} points: {} ms".format(n, execution_time))
        convexHullEdge = []
        n = n + 1

