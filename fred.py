# import full_fred
from full_fred.fred import Fred
import os

api_location = r'C:\Users\jsidd\Documents\fred\fred.txt'

# with open(api_location) as g:
#     api = g.read()

# print(api)

fred = Fred(api_location)

df = fred.get_series_df('GDPPOT')
print(df)

