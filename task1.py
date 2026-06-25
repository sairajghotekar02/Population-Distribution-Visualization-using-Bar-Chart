import pandas as pd
import matplotlib.pyplot as plt

# CSV load
df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_406129.csv", skiprows=4)

# 2023 data
population = df[['Country Name', '2023']].dropna()

# Top 10 countries
top10 = population.sort_values('2023', ascending=False).head(10)

# Bar Chart
plt.figure(figsize=(10,5))
plt.bar(top10['Country Name'], top10['2023'])

plt.title("Top 10 Countries by Population (2023)")
plt.xlabel("Country")
plt.ylabel("Population")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()