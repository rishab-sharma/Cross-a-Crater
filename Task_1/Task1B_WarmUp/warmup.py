import cv2
import numpy as np
grid_line_x = 7
grid_line_y = 7
m=600/(grid_line_x-1)
n=600/(grid_line_y-1)
img_rgb = cv2.imread('demo.jpg')
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
grid_map = [ [ 0 for i in range(grid_line_y-1) ] for j in range(grid_line_x-1) ]
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
for i in range(len(grid_map)):
    for j in range(len(grid_map)):
        if j==5:print grid_map[i][j]
        else:print grid_map[i][j],
cv2.imshow('demo',img_rgb)    
cv2.waitKey(0)
cv2.waitKey(0)


