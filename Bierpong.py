import matplotlib.pyplot as plt
import re

### Daten einlesen
stream = open("spielstandstabelle.csv","r")
outcome_lst = [x.strip() for x in stream]

### Spieler und ergebnislisten generieren
spieler = []
ergebnisliste = []
for line in outcome_lst:
    m = re.search(r"(\w+),(\d\S*)",line)

    if m:
        spieler.append(m.group(1))
        ergebnisliste.append(m.group(2))

#### Plot daten vorbereiten
win_spieler1 = ergebnisliste[0].split(",")
win_spieler2 = ergebnisliste[1].split(",")
y_vec_spieler1 = [0]
y_vec_spieler2 = [0]
Spielrunden = len(win_spieler1)
x_vec = [x for x in range(Spielrunden+1)]
win_count1 = 0
win_count2 = 0

for i,j in enumerate(win_spieler1):
    if i == 0:
        y_vec_spieler1.append(int(j))
    else:
        y_vec_spieler1.append(y_vec_spieler1[i]+int(j))
    if j == "1":
        win_count1 += 1

for i,j in enumerate(win_spieler2):
    if i == 0:
        y_vec_spieler2.append(int(j))
    else:
        y_vec_spieler2.append(y_vec_spieler2[i]+int(j))
    if j == "1":
        win_count2 += 1

win_rate1 = win_count1/Spielrunden *100
win_rate2 = win_count2/Spielrunden *100

assert(len(x_vec) == len(y_vec_spieler1))
assert(len(x_vec) == len(y_vec_spieler2))
####Plot settings
fig, ax = plt.subplots(figsize =(10,6.18))
ax.set_ylabel("Punkte")
ax.set_title("WG Bierpongturnier")
ax.grid(False)
ax.set_ylim(0,Spielrunden)
ax.set_xlim(0,Spielrunden)
ax.plot(x_vec, y_vec_spieler1, color="darkorange",\
        label="{} {:.2f}% win rate".format(spieler[0],win_rate1))
ax.plot(x_vec, y_vec_spieler2, color="k",\
        label="{} {:.2f}% win rate".format(spieler[1],win_rate2))
ax.legend(loc="upper right")
fig.savefig("graphic.pdf")
plt.show()

#fig.savefig("matchpos distances100.pdf",bbox_inches="tight")
