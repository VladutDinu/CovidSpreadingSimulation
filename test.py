import csv
import tensorflow as tf
from tensorflow import keras
from keras.layers import Dense, LSTM, Dropout
import numpy as np
inf=[]
heal=[]
window_size = 5
model = tf.keras.models.load_model('10k120')
with open("data10k120-8locatii-mamaresauegal96.csv", "r") as f:
    reader=csv.reader(f,delimiter=',')
    next(reader)
    for x in reader:
        inf.append(int(x[0]))
        heal.append(int(x[1]))

forecast_inf=[]
forecast_heal=[]
for time in range(len(inf[:]) - window_size):
    forecast_inf.append(model.predict(np.array(inf[time:time + window_size]).reshape(1,window_size)))
    forecast_heal.append(model.predict(np.array(heal[time:time + window_size]).reshape(1,window_size)))


results_inf = np.array(forecast_inf)[:, 0, 0]
results_heal = np.array(forecast_heal)[:, 0, 0]

inf_compare=[]
heal_compare=[]
with open("data10k120-8locatii-maimicsauegal4.csv", "r") as f:
    reader=csv.reader(f,delimiter=',')
    next(reader)
    for x in reader:
        inf_compare.append(int(x[0]))
        heal_compare.append(int(x[1]))



forecast_inf_compare=[]
forecast_heal_compare=[]
for time in range(len(inf[:]) - window_size):
    forecast_inf_compare.append(model.predict(np.array(inf_compare[time:time + window_size]).reshape(1,window_size)))
    forecast_heal_compare.append(model.predict(np.array(heal_compare[time:time + window_size]).reshape(1,window_size)))


results_inf_compare = np.array(forecast_inf_compare)[:, 0, 0]
results_heal_compare = np.array(forecast_heal_compare)[:, 0, 0]
import matplotlib.pyplot as plt
infected=[]
deaths=[]
with open("covid_romania.csv","r") as f:
    reader=csv.reader(f,delimiter=',')
    for x in reader:
        print(x)
        infected.append(int(x[4]))
        deaths.append(int(x[5]))
#print(infected)
for x in range(1,len(infected)):
    infected[x]+=infected[x-1]
    deaths[x]+=deaths[x-1]
infected=[x/50 for x in infected]
deaths=[x/50 for x in deaths]
fig, axs=plt.subplots(3,2, figsize=(24,12))

axs[0][0].plot(inf, label="No. of infected people")
axs[0][0].plot(results_inf, label="No. of predicted infected people")
axs[1][0].plot(heal, label="No. of healty people")
axs[1][0].plot(results_heal, label="No. of predicted healty people")
axs[0][1].plot(inf_compare, label="No. of infected people")
axs[0][1].plot(results_inf_compare, label="No. of predicted infected people")
axs[1][1].plot(heal_compare, label="No. of healty people")
axs[1][1].plot(results_heal_compare, label="No. of predicted healty people")
axs[2][0].plot(infected[:120], label="Real data infected people")
axs[2][1].plot(deaths[:120], label="Real data deaths")
for x in axs:
    for y in x:
        y.legend()
plt.show()


