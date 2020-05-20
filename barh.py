import matplotlib.pyplot as plt
import re
import numpy as np

#y-axis = Spieltage
Matches = ('1','2')
## turns = Length of input Bitvector!
turns = 5
#segments = 2
##first: read turns into lists/numpy arrays, add consecutve numer to 'matches'
###second: try to map data to matches -> np.array(len(Bitvector_spieler1), len(Bitvector_spieler1))

#generate test data
#data = 3 + 10* np.random.rand(segments, len(Matches))
# store np.sum(Bitvector)in ndarray
input = np.array([[2,4], [3,1]], np.int32)
#data = 3 + 10* np.random.rand(segments, len(Matches))
#reinit y_vals to len matches
y_pos = np.arange(1,len(Matches)+1)
plt_array = []
#set width: 0.25
width = 0.25
colors ='rg'
fig, ax = plt.subplots(figsize =(10,6.18))
##loop over arrays and plot bars
left = np.zeros(len(Matches))
for idx, data in enumerate(input):
    plt_array.append(ax.barh(y_pos, data,
      align='center',
      left=left))
    # accumulate the left-hand offsets
    #left += data
ax.set_yticks(y_pos)
ax.set_yticklabels(Matches)
ax.set_xlabel('Match turns')

plt.show()

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
