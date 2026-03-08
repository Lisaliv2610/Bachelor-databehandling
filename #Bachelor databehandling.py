#Bachelor databehandling
import pandas as pd


# Læs data fra CSV-filen
data = pd.read_csv('data.csv')
# Vis de første 5 rækker af data
print(data.head())