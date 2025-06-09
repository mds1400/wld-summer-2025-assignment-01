# %%
import pandas as pd
import matplotlib.pyplot as plt
print("All packages imported successfully!")
 
print(f"Pandas version: {pd.__version__}")
# Test loading the data file
df = pd.read_csv('UNRATE.csv')
print(f"Data loaded successfully! Shape: {df.shape}")

# %%
import pandas as pd
import matplotlib.pyplot as plt
# Load the provided unemployment data
df = pd.read_csv('UNRATE.csv')
df['DATE'] = pd.to_datetime(df['observation_date'])
print("Dataset shape:", df.shape)
print("\nFirst 5 rows:")
df.head()

# %%
print("Data types:")
print(df.dtypes)
print("\nBasic statistics:")
df['UNRATE'].describe()

# %%

import pandas as pd
import matplotlib.pyplot as plt
# Load the provided unemployment data
df = pd.read_csv('UNRATE.csv')
# Convert DATE column to datetime
df['DATE'] = pd.to_datetime(df['observation_date'])
print("Dataset shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nData types:")
print(df.dtypes)

# %%
average_unrate = df["UNRATE"].mean()
print("Average UNRATE:", average_unrate)


# %%
# Highest UNRATE
max_row = df.loc[df["UNRATE"].idxmax()]
print("Highest UNRATE:")
print("  UNRATE:", max_row["UNRATE"])
print("  DATE:  ", max_row["DATE"])

# Lowest UNRATE
min_row = df.loc[df["UNRATE"].idxmin()]
print("\nLowest UNRATE:")
print("  UNRATE:", min_row["UNRATE"])
print("  DATE:  ", min_row["DATE"])


# %%
import pandas as pd

# Ensure DATE column is datetime
df["DATE"] = pd.to_datetime(df["DATE"])

# Create a 'Decade' column
df["Decade"] = (df["DATE"].dt.year // 10) * 10

# Group by decade and calculate summary statistics
decade_stats = df.groupby("Decade")["UNRATE"].agg(["mean", "min", "max", "std", "count"]).reset_index()

# Rename columns for clarity (optional)
decade_stats.columns = ["Decade", "Average UNRATE", "Min UNRATE", "Max UNRATE", "Std Dev", "Count"]

# Display results
print(decade_stats)


# %%
import pandas as pd

# Ensure DATE column is in datetime format
df["DATE"] = pd.to_datetime(df["DATE"])

# Extract the year
df["Year"] = df["DATE"].dt.year

# Group by year and calculate average UNRATE
yearly_avg = df.groupby("Year")["UNRATE"].mean()

# Find the year with the highest average unemployment rate
max_year = yearly_avg.idxmax()
max_value = yearly_avg.max()

print(f"Year with highest average unemployment rate: {max_year}")
print(f"Average UNRATE: {max_value:.2f}")


# %%
# Ensure DATE column is datetime
df["DATE"] = pd.to_datetime(df["DATE"])

# ---- 2008 Financial Crisis (2008–2010) ----
crisis_2008 = df[(df["DATE"] >= "2008-01-01") & (df["DATE"] <= "2010-12-31")]

# Peak UNRATE during crisis
max_2008 = crisis_2008.loc[crisis_2008["UNRATE"].idxmax()]
avg_2008 = crisis_2008["UNRATE"].mean()

print("2008 Financial Crisis:")
print(f"  Peak UNRATE: {max_2008['UNRATE']}% in {max_2008['DATE'].strftime('%B %Y')}")
print(f"  Average UNRATE: {avg_2008:.2f}%\n")

# ---- COVID-19 Pandemic (2020 onward) ----
covid = df[df["DATE"] >= "2020-01-01"]

# Peak UNRATE during COVID
max_covid = covid.loc[covid["UNRATE"].idxmax()]
avg_covid = covid["UNRATE"].mean()

print("COVID-19 Pandemic:")
print(f"  Peak UNRATE: {max_covid['UNRATE']}% in {max_covid['DATE'].strftime('%B %Y')}")
print(f"  Average UNRATE: {avg_covid:.2f}%")


# %%
# Get the row with the lowest standard deviation
lowest_std_row = decade_stats.loc[decade_stats["Std Dev"].idxmin()]

# Print the result
print("Decade with the lowest unemployment rate standard deviation:")
print(lowest_std_row)


# %%
import pandas as pd
import matplotlib.pyplot as plt

# Ensure DATE is in datetime format
df["DATE"] = pd.to_datetime(df["DATE"])

# Extract year
df["Year"] = df["DATE"].dt.year

# Filter for the last 10 years (2015–2025)
last_10_years = df[df["Year"] >= 2015]

# Compute yearly average unemployment rate
yearly_avg = last_10_years.groupby("Year")["UNRATE"].mean().reset_index()

# Print values
print("Average Unemployment Rate (2015–2025):")
print(yearly_avg)

# Plot trend
plt.figure(figsize=(10, 5))
plt.plot(yearly_avg["Year"], yearly_avg["UNRATE"], marker='o', linestyle='-')
plt.title("Trend in Unemployment Rate (2015–2025)")
plt.xlabel("Year")
plt.ylabel("Average UNRATE (%)")
plt.grid(True)
plt.tight_layout()
plt.show()


# %%

import pandas as pd
import matplotlib.pyplot as plt

# Ensure DATE is datetime
df["DATE"] = pd.to_datetime(df["DATE"])

# ------------------------------
# Line Chart: Unemployment Rate Over Time
# ------------------------------
plt.figure(figsize=(12, 6))
plt.plot(df["DATE"], df["UNRATE"], color="blue", linewidth=1)
plt.title("Unemployment Rate Over Time", fontsize=16)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Unemployment Rate (%)", fontsize=12)
plt.grid(True)
plt.tight_layout()

# Save and Show
plt.savefig("unemployment_trend.png", dpi=300)
plt.show()

# ------------------------------
# Bar Chart: Average Unemployment by Decade
# ------------------------------
# Create 'Decade' column
df["Decade"] = (df["DATE"].dt.year // 10) * 10

# Group and compute averages
decade_avg = df.groupby("Decade")["UNRATE"].mean().reset_index()

plt.figure(figsize=(10, 6))
plt.bar(decade_avg["Decade"].astype(str), decade_avg["UNRATE"], color="darkorange")
plt.axhline(y=5.67, color='red', linestyle='--', linewidth=2, label='Average: 5.67%')
plt.title("Average Unemployment Rate by Decade", fontsize=16)
plt.xlabel("Decade", fontsize=12)
plt.ylabel("Average UNRATE (%)", fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.legend()
plt.tight_layout()

# Save and Show
plt.savefig("unemployment_by_decade.png", dpi=300)
plt.show()





# %%



