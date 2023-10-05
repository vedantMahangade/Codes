import random
import time

# list to store input pointspoint_range
points = []

# List to store edges of Convex Hull that is computed
convexHullEdge = []

# Funcation defined to get what side does the point lie with respect to line LR
def whichSide(L, R, point):
    x1, y1 = L
    x2, y2 = R
    x, y = point

    a = y2 - y1
    b = x1 - x2
    c = x2*y1 - x1*y2
    
    # since a plane is defined as function f = ax + by + c
    f = a*x + b*y + c

    if f<0:
        return 'right'
    elif f > 0:
        return 'left'
    else:
        return 'onLine'
    

def ConvexHull(partition, A, B):
    # if there are no points in the partition then return
    if len(partition) == 0:
        return
    
    x1, y1 = A
    x2, y2 = B
    a = y2 - y1
    b = x1 - x2
    c = x2*y1 - x1*y2
    maximumDistance = -1
    C = None

    for point in partition:
        x, y = point
        f = abs(a*x + b*y + c)
        if f>maximumDistance:
            f = maximumDistance
            C = point
    x, y = C

    # Since two new edges are discovered, we remove the previous edge and add the two new ones
    convexHullEdge.remove((A, B))
    convexHullEdge.append((A, C))
    convexHullEdge.append((C, B))

    # Dividing the partition into sub partitions
    # we check if the point lies on right of AC or on right of CB. 
    # if the point lies within the triangle ACB, then we discard those points
    partition.remove(C)
    AC_Right = []
    CB_Right = []
    for point in partition:
        leftOrRightOfAC = whichSide(A, C, point)
        if leftOrRightOfAC =='right':
            AC_Right.append(point)

        leftOrRightOfCB = whichSide(C, B, point)
        if leftOrRightOfCB == 'right':
            CB_Right.append(point)

    # Divide and Conquer logic
    # the set of points is divided in half and recursivly called two times
    ConvexHull(AC_Right, A, C)
    ConvexHull(CB_Right, C, B)

def preProcess():
    # sorts the points based on x-coordinate(k[0]) and then by the y-coordinate(k[1])
    sortedPoints = sorted(points, key = lambda k: [k[0], k[1]])   

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
    ConvexHull(LR_Right, L, R)
    ConvexHull(LR_Left, R, L)



############ Driver Code for execution time calculation ################
if __name__ == '__main__':

    # point_range is the range of the coordinates i.e. the x and y values can go from -5 to 5
    point_range = 5

    # n is the input length that will determine the execution time
    # Creating a while loop which will execute the entire code for different values of n and compute the execution time
    n = 5
    print()
    while n <= 10:
        
        #the loop below stores n random coordinates in the points list.
        for i in range(0, n):
            points.append([random.randint(-1,7), random.randint(-1,7)])
        
        start_time = time.time()
        preProcess()
        execution_time = time.time() - start_time

        # Extracting distinct set of coordinates for printing from list of edges
        convexHullPoints = []
        for edge in convexHullEdge:
            for point in edge:
                if point not in convexHullPoints:
                    convexHullPoints.append(point)

        print("\n------------------------------------------------------------------------------")
        print("Computing Convex Hull for Set P of {} points", n)
        print("\nSet P: ", points)
        print("\nComputed Convex Hull: ", convexHullPoints)
        print("\nTime taken for {} points: {} ms".format(n, execution_time))
        n = n + 1

