import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mftool import Mftool
from IPython.display import display

# Filter MF and list all funds
mf = Mftool()
result = mf.get_available_schemes('hdfc')
for scheme_code, scheme in result.items():
    print(scheme_code, scheme)

# AMFI codes
mf = Mftool()
mutual_fund_code = '118989'
d1 = mf.get_scheme_quote(mutual_fund_code)
d2 = mf.get_scheme_details(mutual_fund_code)
print({**d1, **d2})

# Let’s get the historical NAV data in a pandas dataframe and plot the data :
mutual_fund_code = '118989'
mutual_fund = 'HDFC Mid-Cap Opportunities Fund - Growth Option - Direct Plan'

df = mf.get_scheme_historical_nav(mutual_fund_code,as_Dataframe=True).reset_index()
df['nav'] = df['nav'].astype(float)
df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')
df = df.sort_values('date').reset_index(drop=True)
print(df)
display(df)
df.plot(x='date', y='nav')
plt.title(mutual_fund)
plt.show()

print(df['nav'][0])