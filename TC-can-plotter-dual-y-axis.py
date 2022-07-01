import pandas as pd
import datetime
import time
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats
import statistics

df = pd.read_excel(open('HVS-123_2022-06-24.xlsx', 'rb'), sheet_name='R75355 MultiChannel - Data', skiprows=6)

#df['Timestamp'] = pd.to_datetime(df['Timestamp'])
#df['Timestamp'] = df['Timestamp'].dt.tz_localize(None)

df['Date'] = pd.to_datetime(df['Date'], format='%m/%d-%Y  %H:%M:%s')
#df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%m/%d-%Y  %H:%M:%s')

#df['MD_INFO.MOTOR_SPEED_MA'] = df['MD_INFO.MOTOR_SPEED'].rolling(window=50, center=True, min_periods=5).mean()

fig, ax1 = plt.subplots()
ax1.plot(df['Time'], df['Thermocouple 1 (°C)'], label='LG69T surface')
ax1.plot(df['Time'], df['Thermocouple 2 (°C)'], label='Speaker magnet')
ax1.plot(df['Time'], df['Thermocouple 3 (°C)'], label='SC top ambient')
ax1.plot(df['Time'], df['Thermocouple 4 (°C)'], label='SC bot ambient')
ax1.plot(df['Time'], df['Thermocouple 5 (°C)'], label='SC cover inside surface')
ax1.plot(df['Time'], df['Thermocouple 6 (°C)'], label='SC cover outside surface')
ax1.plot(df['Time'], df['Thermocouple 7 (°C)'], label='Cockpit ambient')
ax1.plot(df['Time'], df['Thermocouple 8 (°C)'], label='Cockpit cover inside')
ax1.plot(df['Time'], df['Thermocouple 9 (°C)'], label='Cockpit cover outside')
ax1.plot(df['Time'], df['Thermocouple 10 (°C)'], label='Chamber right side ambient')
ax1.plot(df['Time'], df['Thermocouple 11 (°C)'], label='Chamber left side ambient')
ax1.plot(df['Time'], df['Thermocouple 12 (°C)'], label='Chamber middle ambient')

#ax2 = ax1.twinx()

#ax2.plot(df['Timestamp'], df['MD_INFO.MOTOR_SPEED'], label="MD_INFO.MOTOR_SPEED (RPM)", color='m')
#ax2.plot(df['Timestamp'], df['SC_STATUS.STATE'], label="SC_STATUS.STATE")

# In order to fit legend below plot, shrink axis height by 10% on the bottom
box = ax1.get_position()
ax1.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])
#box = ax2.get_position()
#ax2.set_position([box.x0, box.y0 + box.height * 0.1,
#                 box.width, box.height * 0.9])

# Put a legend below plot
ax1.legend(loc='upper center', bbox_to_anchor=(0.5, -0.13),
          fancybox=True, shadow=True, ncol=5)
#ax2.legend(loc='upper center', bbox_to_anchor=(0.5, -0.22),
#          fancybox=True, shadow=True, ncol=5)

# Rotate x axis labels
ax1.tick_params(axis='x', labelrotation=45)


ax1.set_ylim([0, 120])
#ax2.set_ylim([-100, 2400])
#ax1.set_yticks(np.arange(20, 100, 5))
#ax2.set_yticks(np.arange(0, 2500, 100))
ax1.set_ylabel("Temperature (°C)")
#ax2.set_ylabel("Motor Speed (RPM)")
plt.xlabel("Date-time")
plt.title("Thermocouple Temp Data vs. Time")
plt.suptitle("HVS-123 Galaxy System Controller - Chamber Thermal Stress Test")
plt.grid(True)

plt.show()
