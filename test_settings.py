import matplotlib.pyplot as plt
import numpy as np

##README: just tests for functionality. No input specification or plot
#generating via loops.

## create data lists
Matches = [1,2,3]
#turns = len(Bitvector)
turns =[5,3,5]
max_turns = np.max(turns)
print(Matches)
print(max_turns)
#x_vals
player1 = [2,3,4]
player2 =  [3,0,1]
#y_vals
y = np.arange(len(player1))

#plot settings#
y_labels = Matches[::-1]
print(y_labels)
plt.barh(y,player1, color="grey")
plt.barh(y,player2, color="yellow", left=player1)
plt.xticks(np.arange(1,max_turns+1))
plt.yticks(y, y_labels)
plt.grid(axis="x")
plt.show()
