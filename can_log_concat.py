import glob2 as glob
import pandas as pd
import matplotlib.dates

# Return all csv files under the root directory using glob module and store in new DF
files = glob.glob("hvs-123/*/*")
df = pd.concat([pd.read_csv(f) for f in files])

# Convert timestamp column to datetime format and remove timezone information
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df['Timestamp'] = df['Timestamp'].dt.tz_localize(None)

# Write concatenated df to new csv file
df.to_csv("files_concatenated.csv")
