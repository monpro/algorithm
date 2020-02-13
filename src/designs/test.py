import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
# Example authenticated client (needed for non-public datasets):
client = Socrata("data.cityofnewyork.us",
                 app_token="auoZNB0hy6vhbqxl1rl6x9omb")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.

results = client.get("8h9b-rp9u",where='latitude<40.68057048300005')

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

print(results_df)