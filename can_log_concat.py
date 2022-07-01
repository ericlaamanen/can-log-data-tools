import glob2 as glob
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.dates

# Return all csv files under the root directory using glob module and store in new DF
files = glob.glob("hvs-123/*/*")
df = pd.concat([pd.read_csv(f) for f in files])

df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df['Timestamp'] = df['Timestamp'].dt.tz_localize(None)

#df['Timestamp'] = pd.to_datetime(df.Timestamp, format = '%Y-%m-%d %H:%M:%S%z')
#df['Timestamp'] = df['Timestamp'].dt.strftime("%Y-%m-%d %H:%M:%S")

df.to_csv("files_concatenated.csv")

fig, ax1 = plt.subplots()

#df['Timestamp'] = matplotlib.dates.date2num(df['Timestamp'])

#ax1.plot(df['Timestamp'], df['SC_IMU_GYRO.ROLL'], label='SC_IMU_GYRO.ROLL')
#ax1.plot(df['Timestamp'], df['SC_IMU_GYRO.PITCH'], label='SC_IMU_GYRO.PITCH')
#ax1.plot(df['Timestamp'], df['SC_IMU_GYRO.YAW'], label='SC_IMU_GYRO.YAW')

#ax1.plot(df['Timestamp'], df['SC_IMU_ACC.X'], label='SC_IMU_ACC.X')
#ax1.plot(df['Timestamp'], df['SC_IMU_ACC.Y'], label='SC_IMU_ACC.Y')
#ax1.plot(df['Timestamp'], df['SC_IMU_ACC.Z'], label='SC_IMU_ACC.Z')

#ax1.plot(df['Timestamp'], df['GPS_OTHER.NSAT'], label='Number of Satellites')
#ax1.plot(df['Timestamp'], df['RADIO_TELEMETRY.RSSI'], label='Radio Telemetry RSSI')
#ax1.plot(df['Timestamp'], df['RADIO_TELEMETRY.RADIO_DRIVER_STATE'], label='Radio Telemetry Radio Driver State')
#ax1.plot(df['Timestamp'], df['RADIO_TELEMETRY.RADIO_STATE'], label='Radio Telemetry Radio State')
#ax1.plot(df['Timestamp'], df['BMS_STATUS.SOC'], label="Battery_SOC")

#ax1.plot(df['Timestamp'], df['BMS_STATUS.SOC'], label="BMS_STATUS.SOC")
#ax1.plot(df['Timestamp'], df['BMS_BATTERY_VOLTAGE.BQ_BAT_V'], label="BMS_BATTERY_VOLTAGE.BQ_BAT_V")
#ax1.plot(df['Timestamp'], df['BMS_BATTERY_VOLTAGE.VOLTAGE'], label="BMS_BATTERY_VOLTAGE.VOLTAGE")
ax1.plot(df['Timestamp'], df['MD_IMU_MOTORSPEED.MOTOR_SPEED'], label="MD_IMU_MOTORSPEED.MOTOR_SPEED (RPM)")
#ax1.plot(df['Timestamp'], df['BMS_INFO.BUS_CURRENT'], label="BMS_INFO.BUS_CURRENT (A)")

# In order to fit legend below plot, shrink axis height by 10% on the bottom
box = ax1.get_position()
ax1.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])

# Put a legend below plot
ax1.legend(loc='upper center', bbox_to_anchor=(0.5, -0.16),
          fancybox=True, shadow=True, ncol=5)

ax1.tick_params(axis='x', labelrotation=45)

#ax1.set_ylim([-15, 5])
#ax1.set_ylabel("Battery %")
plt.xlabel("Timestamp")

plt.title("CAN parameters vs. Time")
plt.suptitle("HVS-109 - Galaxy System Controller")
plt.grid(True)

plt.show()