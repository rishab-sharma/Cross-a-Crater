# -*- coding: utf-8 -*-
"""
**************************************************************************
*                  IMAGE PROCESSING (e-Yantra 2016)
*                  ================================
*  This software is intended to teach image processing concepts
*
*  MODULE: Task1C
*  Filename: getCellVal.py
*  Version: 1.0.0  
*  Date: October 13, 2016
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
# detectCellVal detects the numbers/operatorsm,
# perform respective expression evaluation
# and stores them into the grid_map 
# detectCellVal(img,grid_map)

# Find the number/operators, perform the calculations and store the result into the grid_map
# Return the resultant grid_map
import cv2
import numpy as np
# comment here
def detectCellVal(img_rgb,grid_map):
    zero = cv2.imread('digits/0.jpg')
    one = cv2.imread('digits/1.jpg')
    two = cv2.imread('digits/2.jpg')
    three = cv2.imread('digits/3.jpg')
    four = cv2.imread('digits/4.jpg')
    five = cv2.imread('digits/5.jpg')
    six = cv2.imread('digits/6.jpg')
    seven = cv2.imread('digits/7.jpg')
    eight = cv2.imread('digits/8.jpg')
    nine = cv2.imread('digits/9.jpg')
    plus = cv2.imread('digits/plus.jpg')
    minus = cv2.imread('digits/minus.jpg')
    ############################################################
    for i in range(6):
        for j in range(6):
            px = img_rgb[((100*i)+5):((100*i)+95),((100*j)+5):((100*j)+95)]
            d1 = cv2.subtract(px,zero[5:95,5:95])
            gray = cv2.cvtColor(d1,cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(gray, 220,255,cv2.THRESH_BINARY)
            r = not np.any(mask)
            if r == True:
                grid_map[i][j]=0
            d1 = cv2.subtract(px,one[5:95,5:95])
            gray = cv2.cvtColor(d1,cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(gray, 220,255,cv2.THRESH_BINARY)
            r = not np.any(mask)
            if r == True:
                grid_map[i][j]=1
            d1 = cv2.subtract(px,two[5:95,5:95])
            gray = cv2.cvtColor(d1,cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(gray, 220,255,cv2.THRESH_BINARY)
            r = not np.any(mask)
            if r == True:
                grid_map[i][j]=2
            d1 = cv2.subtract(px,three[5:95,5:95])
            gray = cv2.cvtColor(d1,cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(gray, 220,255,cv2.THRESH_BINARY)
            r = not np.any(mask)
            if r == True:
                grid_map[i][j]=3
            d1 = cv2.subtract(px,four[5:95,5:95])
            gray = cv2.cvtColor(d1,cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(gray, 220,255,cv2.THRESH_BINARY)
            r = not np.any(mask)
            if r == True:
                grid_map[i][j]=4
            d1 = cv2.subtract(px,five[5:95,5:95])
            gray = cv2.cvtColor(d1,cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(gray, 220,255,cv2.THRESH_BINARY)
            r = not np.any(mask)
            if r == True:
                grid_map[i][j]=5
            d1 = cv2.subtract(px,six[5:95,5:95])
            gray = cv2.cvtColor(d1,cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(gray, 220,255,cv2.THRESH_BINARY)
            r = not np.any(mask)
            if r == True:
                grid_map[i][j]=6
            d1 = cv2.subtract(px,seven[5:95,5:95])
            gray = cv2.cvtColor(d1,cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(gray, 220,255,cv2.THRESH_BINARY)
            r = not np.any(mask)
            if r == True:
                grid_map[i][j]=7
            d1 = cv2.subtract(px,eight[5:95,5:95])
            gray = cv2.cvtColor(d1,cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(gray, 220,255,cv2.THRESH_BINARY)
            r = not np.any(mask)
            if r == True:
                grid_map[i][j]=8
            d1 = cv2.subtract(px,nine[5:95,5:95])
            gray = cv2.cvtColor(d1,cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(gray, 220,255,cv2.THRESH_BINARY)
            r = not np.any(mask)
            if r == True:
                grid_map[i][j]=9
            d1 = cv2.subtract(px,plus[5:95,5:95])
            gray = cv2.cvtColor(d1,cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(gray, 220,255,cv2.THRESH_BINARY)
            r = not np.any(mask)
            if r == True:
                grid_map[i][j]= "+"
            d1 = cv2.subtract(px,minus[5:95,5:95])
            gray = cv2.cvtColor(d1,cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(gray, 220,255,cv2.THRESH_BINARY)
            r = not np.any(mask)
            if r == True and grid_map[i][j]!= "+":
                grid_map[i][j]= "-"
    for i in range(0,6):
        for j in range(0,6):
            if grid_map[i][1] == '+' and grid_map[i][3] == '-':
                 grid_map[i][5] = grid_map[i][0] + grid_map[i][2] - grid_map[i][4]
            elif grid_map[i][1] == '+' and grid_map[i][3] == '+':
                 grid_map[i][5] = grid_map[i][0] + grid_map[i][2] + grid_map[i][4]
            elif grid_map[i][1] == '-' and grid_map[i][3] == '-':
                 grid_map[i][5] = grid_map[i][0] - grid_map[i][2] - grid_map[i][4]
            elif grid_map[i][1] == '-' and grid_map[i][3] == '+':
                 grid_map[i][5] = grid_map[i][0] - grid_map[i][2] + grid_map[i][4]
    return grid_map
