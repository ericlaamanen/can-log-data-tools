# Tool for plotting thermocouple data from Omega OM-CP Data Logger software and adding CAN data to the same plot on an additional Y axis.

import pandas as pd
import datetime
import numpy as np
from matplotlib import pyplot as plt
import statistics

df = pd.read_excel(open('filename.xlsx', 'rb'), sheet_name='R75355 MultiChannel - Data', skiprows=6)

#df['Timestamp'] = pd.to_datetime(df['Timestamp'])
#df['Timestamp'] = df['Timestamp'].dt.tz_localize(None)

df['Date'] = pd.to_datetime(df['Date'], format='%m/%d-%Y  %H:%M:%s')
#df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%m/%d-%Y  %H:%M:%s')

# Optionally apply rolling average to data column(s)
#df['MD_INFO.MOTOR_SPEED_MA'] = df['MD_INFO.MOTOR_SPEED'].rolling(window=50, center=True, min_periods=5).mean()

fig, ax1 = plt.subplots()
ax1.plot(df['Time'], df['Thermocouple 1 (°C)'], label='Thermocouple 1')
ax1.plot(df['Time'], df['Thermocouple 2 (°C)'], label='Thermocouple 2')
ax1.plot(df['Time'], df['Thermocouple 3 (°C)'], label='Thermocouple 3')
ax1.plot(df['Time'], df['Thermocouple 4 (°C)'], label='Thermocouple 4')
ax1.plot(df['Time'], df['Thermocouple 5 (°C)'], label='Thermocouple 5')
ax1.plot(df['Time'], df['Thermocouple 6 (°C)'], label='Thermocouple 6')
ax1.plot(df['Time'], df['Thermocouple 7 (°C)'], label='Thermocouple 7')
ax1.plot(df['Time'], df['Thermocouple 8 (°C)'], label='Thermocouple 8')
ax1.plot(df['Time'], df['Thermocouple 9 (°C)'], label='Thermocouple 9')

# Create an additional Y axis  positioned opposite to regular Y axis
ax2 = ax1.twinx()

# Plot desired CAN parameters on second Y axis
ax2.plot(df['Timestamp'], df['MD_INFO.MOTOR_SPEED'], label="MD_INFO.MOTOR_SPEED (RPM)", color='m')

# In order to fit legend below plot, shrink axis height by 10% on the bottom
box = ax1.get_position()
ax1.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])
box = ax2.get_position()
#ax2.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])

# Place a legend below plot
ax1.legend(loc='upper center', bbox_to_anchor=(0.5, -0.13),
          fancybox=True, shadow=True, ncol=5)
ax2.legend(loc='upper center', bbox_to_anchor=(0.5, -0.22),
          fancybox=True, shadow=True, ncol=5)

# Rotate x axis labels
ax1.tick_params(axis='x', labelrotation=45)

ax1.set_ylim([0, 120])
ax2.set_ylim([-100, 2400])
ax1.set_ylabel("Temperature (°C)")
ax2.set_ylabel("Motor Speed (RPM)")
plt.xlabel("Date-time")
plt.title("Thermocouple Temp Data vs. Time")
plt.suptitle("Insert ticket number and test description here")
plt.grid(True)

plt.show()
