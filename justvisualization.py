import csv
import numpy as np
import matplotlib.pyplot as plt
inf=[]
heal=[]
rec=[]
dead=[]
with open("data.csv", "r") as f:
    reader=csv.reader(f,delimiter=',')
    next(reader)
    for x in reader:
        inf.append(int(x[0]))
        heal.append(int(x[1]))
        rec.append(int(x[2]))
        dead.append(int(x[3]))

fig, axs=plt.subplots(4, figsize=(24,12))

axs[0].plot(inf, label="No. of infected people")
axs[1].plot(heal, label="No. of healty people")
axs[2].plot(rec, label="No. of recovered people")
axs[3].plot(dead, label="No. of dead people")
for x in axs:
    x.legend()
plt.show()


