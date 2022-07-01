

import pandas as pd
import datetime
import time
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats
import statistics

df = pd.read_excel(open('filename.xlsx', 'rb'), sheet_name='R75355 MultiChannel - Data', skiprows=6)

df['Date'] = pd.to_datetime(df['Date'], format='%m/%d-%Y  %H:%M:%s')

# Optionally apply rolling average to data column(s)
# df['MD_INFO.MOTOR_SPEED_MA'] = df['MD_INFO.MOTOR_SPEED'].rolling(window=50, center=True, min_periods=5).mean()

fig, ax = plt.subplots()
ax.plot(df['Time'], df['Thermocouple 1 (°C)'], label='Thermocouple 1')
ax.plot(df['Time'], df['Thermocouple 2 (°C)'], label='Thermocouple 2')
ax.plot(df['Time'], df['Thermocouple 3 (°C)'], label='Thermocouple 3')
ax.plot(df['Time'], df['Thermocouple 4 (°C)'], label='Thermocouple 4')
ax.plot(df['Time'], df['Thermocouple 5 (°C)'], label='Thermocouple 5')
ax.plot(df['Time'], df['Thermocouple 6 (°C)'], label='Thermocouple 6')
ax.plot(df['Time'], df['Thermocouple 7 (°C)'], label='Thermocouple 7')
ax.plot(df['Time'], df['Thermocouple 8 (°C)'], label='Thermocouple 8')
ax.plot(df['Time'], df['Thermocouple 9 (°C)'], label='Thermocouple 9')

# In order to fit legend below plot, shrink axis height by 10% on the bottom
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])

# Place legend below plot
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.13),
          fancybox=True, shadow=True, ncol=5)


# Rotate x axis labels
ax.tick_params(axis='x', labelrotation=45)

ax.set_ylim([0, 120])
ax.set_yticks(np.arange(20, 100, 5))
ax.set_ylabel("Temperature (°C)")
plt.xlabel("Date-time")
plt.title("Thermocouple Temp Data vs. Time")
plt.suptitle("Insert ticket number and test description here")
plt.grid(True)

plt.show()
