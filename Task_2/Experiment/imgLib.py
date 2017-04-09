# -*- coding: utf-8 -*-
"""
**************************************************************************
*                  Cross_A_Crater (e-Yantra 2016)
*                  ================================
*  This software is intended to teach image processing concepts
*
*  MODULE: Task2
*  Filename: imgLib.py
*  Version: 1.5.0  
*  Date: November 21, 2016
*  
*  Author: Jayant Solanki, e-Yantra Project, Department of Computer Science
*  and Engineering, Indian Institute of Technology Bombay.
*  
*  Software released under Creative Commons CC BY-NC-SA
*
*  For legal information refer to:
*        http://creativecommons.org/licenses/by-nc-sa/4.0/legalcode 
*     
*
*  This software is made available on an “AS IS WHERE IS BASIS”. 
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using 
*  ICT(NMEICT)
*
**************************************************************************
"""
"""
* Team Id : < 4785 >
* Author List : < Rishab Sharma >
* Filename: <imgLib.py>
* Theme: <Cross a crator>
* Functions: <detectCellVal ,solveGrid >
* Global Variables: <img_rgb , grid_map , rote_path , rote_length , route_array>
"""
#Complete the both function mentioned below, and return the desired outputs
#Additionally you may add your own methods here to help both methods mentioned below
###################Do not add any external libraries#######################
from heapq import heappush, heappop # for priority queue
import math
import cv2
import numpy as np
# detectCellVal detects the numbers/operatorsm,
# perform respective expression evaluation
# and stores them into the grid_map 
# detectCellVal(img,grid_map)
# Find the number/operators, perform the calculations and store the result into the grid_map
# Return the resultant grid_map
"""
# Function Name: <detectCellVal>
# Input: < img_rgb,grid_map>
# Output: < grid_map>
# Logic: <detectCellVal detects the numbers/operatorsm, perform respective expression evaluation and stores them into the grid_map >
# Example Call: <detectCellVal(img_rgb,grid_map)>
"""
def detectCellVal(img_rgb,grid_map):
        zero = cv2.imread('digits/0.jpg')
        one = cv2.imread('digits/1.jpg')
        for i in range(14):
                for j in range(14):
                    px = img_rgb[((50*i)+5):((50*i)+45),((50*j)+5):((50*j)+45)]
                    d1 = cv2.subtract(px,zero[5:45,5:45])
                    gray = cv2.cvtColor(d1,cv2.COLOR_BGR2GRAY)
                    ret, mask = cv2.threshold(gray, 220,255,cv2.THRESH_BINARY)
                    r = not np.any(mask)
                    if r == True:
                        grid_map[i][j]=1
                    d1 = cv2.subtract(px,one[5:45,5:45])
                    gray = cv2.cvtColor(d1,cv2.COLOR_BGR2GRAY)
                    ret, mask = cv2.threshold(gray, 220,255,cv2.THRESH_BINARY)
                    r = not np.any(mask)
                    if r == True:
                        grid_map[i][j]=0
        return grid_map
############################################################################################
# solveGrid finds the shortest path,
# between valid grid cell in the start row 
# and valid grid cell in the destination row 
# solveGrid(grid_map)
# Return the route_path and route_length
"""
# Function Name: <solveGrid>
# Input: < grid_map >
# Output: < route_path, route_length , route_array >
# Logic: <solveGrid finds the shortest path, between valid grid cell in the start row and valid grid cell in the destination row  >
# Example Call: <def solveGrid(grid_map)>
"""
route_array = []
def solveGrid(grid_map):
        route_length=0
        route_path=[]
        start = []
        end = []
        launch = 0
        dest = 0
        def drone_m():
                return grid_map
        for j in range(14):
                if grid_map[13][j]==0:
                   start.append(j)
                   launch = launch + 1
        for j in range(14):
                if grid_map[0][j]==0:
                   end.append(j)
                   dest = dest + 1
        mini = 1000000
        route_array = []
        for l in start:
                for d in end:
                        class node:
                            xPos = 0 # x position
                            yPos = 0 # y position
                            distance = 0 # total distance already travelled to reach the node
                            priority = 0 # priority = distance + remaining distance estimate
                            def __init__(self, xPos, yPos, distance, priority):
                                self.xPos = xPos
                                self.yPos = yPos
                                self.distance = distance
                                self.priority = priority
                            def __lt__(self, other): # comparison method for priority queue
                                return self.priority < other.priority
                            def updatePriority(self, xDest, yDest):
                                self.priority = self.distance + self.estimate(xDest, yDest) * 10 # A*
                            # give higher priority to going straight instead of diagonally
                            def nextMove(self, dirs, d): # d: direction to move
                                if dirs == 8 and d % 2 != 0:
                                    self.distance += 14
                                else:
                                    self.distance += 10
                            # Estimation function for the remaining distance to the goal.
                            def estimate(self, xDest, yDest):
                                xd = xDest - self.xPos
                                yd = yDest - self.yPos
                                # Euclidian Distance
                                d = math.sqrt(xd * xd + yd * yd)
                                return(d)
                        # The path returned will be a string of digits of directions.
                        def pathFind(grid_map, n, m, dirs, dx, dy, xA, yA, xB, yB):
                            closed_nodes_map = [] # map of closed (tried-out) nodes
                            open_nodes_map = [] # map of open (not-yet-tried) nodes
                            dir_map = [] # map of dirs
                            row = [0] * n
                            for i in range(m): # create 2d arrays
                                closed_nodes_map.append(list(row))
                                open_nodes_map.append(list(row))
                                dir_map.append(list(row))

                            pq = [[], []] # priority queues of open (not-yet-tried) nodes
                            pqi = 0 # priority queue index
                            n0 = node(xA, yA, 0, 0)
                            n0.updatePriority(xB, yB)
                            heappush(pq[pqi], n0)
                            open_nodes_map[yA][xA] = n0.priority # mark it on the open nodes map

                            while len(pq[pqi]) > 0:
                                # get the current node w/ the highest priority
                                # from the list of open nodes
                                n1 = pq[pqi][0] # top node
                                n0 = node(n1.xPos, n1.yPos, n1.distance, n1.priority)
                                x = n0.xPos
                                y = n0.yPos
                                heappop(pq[pqi]) # remove the node from the open list
                                open_nodes_map[y][x] = 0
                                closed_nodes_map[y][x] = 1 # mark it on the closed nodes map

                                # quit searching when the goal is reached
                                # if n0.estimate(xB, yB) == 0:
                                if x == xB and y == yB:
                                    # generate the path from finish to start
                                    # by following the dirs
                                    path = ''
                                    while not (x == xA and y == yA):
                                        j = dir_map[y][x]
                                        c = str((j + dirs / 2) % dirs)
                                        path = c + path
                                        x += dx[j]
                                        y += dy[j]
                                    return path

                                # generate moves (child nodes) in all possible dirs
                                for i in range(dirs):
                                    xdx = x + dx[i]
                                    ydy = y + dy[i]
                                    if not (xdx < 0 or xdx > n-1 or ydy < 0 or ydy > m - 1
                                            or grid_map[ydy][xdx] == 1 or closed_nodes_map[ydy][xdx] == 1):
                                        # generate a child node
                                        m0 = node(xdx, ydy, n0.distance, n0.priority)
                                        m0.nextMove(dirs, i)
                                        m0.updatePriority(xB, yB)
                                        # if it is not in the open list then add into that
                                        if open_nodes_map[ydy][xdx] == 0:
                                            open_nodes_map[ydy][xdx] = m0.priority
                                            heappush(pq[pqi], m0)
                                            # mark its parent node direction
                                            dir_map[ydy][xdx] = (i + dirs / 2) % dirs
                                        elif open_nodes_map[ydy][xdx] > m0.priority:
                                            # update the priority
                                            open_nodes_map[ydy][xdx] = m0.priority
                                            # update the parent direction
                                            dir_map[ydy][xdx] = (i + dirs / 2) % dirs
                                            # replace the node
                                            # by emptying one pq to the other one
                                            # except the node to be replaced will be ignored
                                            # and the new node will be pushed in instead
                                            while not (pq[pqi][0].xPos == xdx and pq[pqi][0].yPos == ydy):
                                                heappush(pq[1 - pqi], pq[pqi][0])
                                                heappop(pq[pqi])
                                            heappop(pq[pqi]) # remove the target node
                                            # empty the larger size priority queue to the smaller one
                                            if len(pq[pqi]) > len(pq[1 - pqi]):
                                                pqi = 1 - pqi
                                            while len(pq[pqi]) > 0:
                                                heappush(pq[1-pqi], pq[pqi][0])
                                                heappop(pq[pqi])       
                                            pqi = 1 - pqi
                                            heappush(pq[pqi], m0) # add the better node instead
                            return '' # if no route found

                        # MAIN
                        dirs = 8 # number of possible directions to move on the map
                        if dirs == 4:
                            dx = [1, 0, -1, 0]
                            dy = [0, 1, 0, -1]
                        elif dirs == 8:
                            dx = [1, 1, 0, -1, -1, -1, 0, 1]
                            dy = [0, 1, 1, 1, 0, -1, -1, -1]

                        n = 14 # horizontal size of the map
                        m = 14# vertical size of the map
                        xA=l
                        yA=13
                        xB=d
                        yB=0
                        route = pathFind(grid_map, n, m, dirs, dx, dy, xA, yA, xB, yB)
                        t = len(route)
                        if t < mini and t > 12:
                                mini = t
                                fA = l
                                fB = d
                                route_array = []
                                for y in range(m):
                                    for x in range(n):
                                        if grid_map[y][x] == 2:
                                                grid_map[y][x] = 1
                                        elif grid_map[y][x] == 3:
                                                grid_map[y][x] = 1
                                        elif grid_map[y][x] == 4:
                                                grid_map[y][x] = 1
                                # mark the route on the map
                                if len(route) > 0:
                                    x = xA
                                    y = yA
                                    grid_map[y][x] = 2
                                    for i in range(len(route)):
                                        j = int(route[i])
                                        x += dx[j]
                                        y += dy[j]
                                        grid_map[y][x] = 3
                                    grid_map[y][x] = 4

                                for y in range(m):
                                    for x in range(n):
                                        xy = grid_map[y][x]
                                        if xy == 2:
                                            route_array.append(y)
                                            route_array.append(x)# start
                                        elif xy == 3:
                                            route_array.append(y)
                                            route_array.append(x)# route
                                        elif xy == 4:
                                            route_array.append(y)
                                            route_array.append(x)# finish
                                route_array.reverse()
        i=0
        while i+1 < len(route_array):
                route_path.append('(' + str(route_array[i]+1) + ',' + str(route_array[i+1]+1) + ')')
                i +=2
        if mini != 1000000:  
              route_length = mini
        else:
                 route_length = 0
        return route_path, route_length , route_array 

############################################################################################
