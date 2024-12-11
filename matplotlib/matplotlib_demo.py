import matplotlib.pyplot as plt
import numpy as np

xPoints = np.array([0,6])
yPoints = np.array([0,250])

#for line
# plt.plot(xPoints , yPoints)

#for points
# plt.plot(xPoints , yPoints , 'o')

# plt.show()

#multiple points
xPoints = np.array([1,3,6,10])
yPoints = np.array([4,2,8,20])

# plt.plot(xPoints , yPoints , 'o')
#plt.plot(yPoints)  #default x value according to y axis , 0,1,2,3,4
#plt.show()


# with marker
# plt.plot(xPoints , yPoints , marker = '*')
# plt.show()


#marker|line|color
#o:r  marker o , line dotted , color red

# plt.plot(xPoints , yPoints , 'D:r')  # diamond marker dotted line red color
# plt.show()

#marker size ms # marker edge color mec # marker face color
#  mfc # line style  'dotted' 'dashed' #linecolor 'r' or '#4CAF50' #linewidth,
#labels #title # font for title and label #grid

plt.plot(xPoints, yPoints , marker = 'o' , ms = 20 , mec = 'y' ,
          mfc = 'c' , linestyle = 'solid', color = 'hotpink', linewidth = '5')

font1 = {'family':'serif','color':'blue','size':12}
font2 = {'family':'serif','color':'darkred','size':15}

plt.xlabel("Average" , fontdict=font1)
plt.ylabel("Total", fontdict=font1)
plt.title("Demo Graph", fontdict=font2 , loc= 'left')
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.grid(axis= 'x')


plt.show()



# multiple lines
# x1 = np.array([0, 1, 2, 3])
# y1 = np.array([3, 8, 1, 10])
# x2 = np.array([0, 1, 2, 3])
# y2 = np.array([6, 2, 7, 11])

# plt.plot(x1, y1, x2, y2)
# plt.show()




