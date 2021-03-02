import matplotlib.pyplot as plt
import csv
infected=[]
deaths=[]
with open("covid_romania.csv","r") as f:
    reader=csv.reader(f,delimiter=',')
    for x in reader:
        #print(x)
        infected.append(int(x[4]))
        deaths.append(int(x[5]))
#print(infected)
for x in range(1,len(infected)):
    infected[x]+=infected[x-1]
    deaths[x]+=deaths[x-1]

fig,axs=plt.subplots(2,figsize=(24,12))
axs[0].plot(infected, label="infected")
axs[1].plot(deaths, label="deaths")
for x in axs:
    x.legend()
plt.show()
