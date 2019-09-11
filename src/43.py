import pandas as pd
pd.set_option('display.mpl_style', 'default') # Make the graphs a bit prettier
figsize(15, 5)
broken_df = pd.read_csv('../data/bikes.csv')
# Look at the first 3 rows
broken_df[:3]