import matplotlib.pyplot as plt
import re
import numpy as np


###### y label = Spieltgage


####Plot settings
#fig, ax = plt.subplots(figsize =(10,6.18))
'''
ax.set_yticks(y_pos)
ax.set_yticklabels(y_pos)
ax.invert_yaxis() # read labels top-to bottum
ax.set_xlabel("x-Achse")
ax.barh(y_pos, x_werte, align="center") # Horizontal bar plot
#ax.legend(loc="upper right")
#fig.savefig("graphic.pdf")
plt.show()
'''
#y-axis = Spieltage
#people = ('A','B','C','D','E','F','G','H')
Matches = ('1','2','3')
## turns = Length of input Bitvector!
turns = 5
#segments = 4
segments = len(Matches)
#X-werte: numpy array of Length turns
x = np.arange(1,turns+1)


data = 3 + 10* np.random.rand(segments, len(Matches))
y_pos = np.arange(len(Matches))
print(f"data= {data}\ny_val={y_pos}")
'''
# generate some multi-dimensional data & arbitrary labels
data = 3 + 10* np.random.rand(segments, len(people))
percentages = (np.random.randint(5,20, (len(people), segments)))
y_pos = np.arange(len(people))
'''
'''
###  Example Data input as Bitvector
#### Problems: Number of rounds per Game may differ!
fig = plt.figure(figsize=(10,6.8))
ax = fig.add_subplot(111)

colors ='rgbmc'
patch_handles = []
#left = np.zeros(len(people)) # left alignment of data starts at zero
left = np.zeros(len(Matches))
for i, d in enumerate(data):
    patch_handles.append(ax.barh(y_pos, d,
      color=colors[i%len(colors)], align='center',
      left=left))
    # accumulate the left-hand offsets
    left += d

# go through all of the bar segments and annotate
for j in range(len(patch_handles)):
    for i, patch in enumerate(patch_handles[j].get_children()):
        bl = patch.get_xy()
        x = 0.5*patch.get_width() + bl[0]
        y = 0.5*patch.get_height() + bl[1]
        ax.text(x,y, "%d%%" % (percentages[i,j]), ha='center')

ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.set_xlabel('Distance')


plt.show()
'''
