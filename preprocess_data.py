import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("timing_data.csv")

# Display basic stats before cleaning
print("Initial Data Overview:")
print(df.describe())

# Remove outliers using Z-score method
def remove_outliers(df, column, threshold=3):
    mean = df[column].mean()
    std = df[column].std()
    df = df[np.abs((df[column] - mean) / std) < threshold]
    return df

df_clean = remove_outliers(df, "time_ns")

# Normalize timing values (Min-Max Scaling)
df_clean["time_ns"] = (df_clean["time_ns"] - df_clean["time_ns"].min()) / (
    df_clean["time_ns"].max() - df_clean["time_ns"].min()
)

# Save cleaned data
df_clean.to_csv("processed_timing_data.csv", index=False)

print(f"Preprocessing complete. Cleaned data saved to processed_timing_data.csv")
