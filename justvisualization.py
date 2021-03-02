import csv
import numpy as np
import matplotlib.pyplot as plt
inf=[]
heal=[]
rec=[]
with open("data-hospital-10k120.csv", "r") as f:
    reader=csv.reader(f,delimiter=',')
    next(reader)
    for x in reader:
        inf.append(int(x[0]))
        heal.append(int(x[1]))
        rec.append(int(x[2]))
for x in range(1,len(inf)):
    rec[x]+=rec[x-1]

fig, axs=plt.subplots(3, figsize=(24,12))

axs[0].plot(inf, label="No. of infected people")
axs[1].plot(heal, label="No. of healty people")
axs[2].plot(rec, label="No. of recovered people")
for x in axs:
    x.legend()
plt.show()


