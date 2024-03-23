# %%
# Loading in packages
import pandas as pd
import numpy as np

# %%
# Loading in data
url = ""
df = pd.read_json(url)

# %%
#### Exercise 1 ####

# How many rows are there? How many columns?
df.shape  # This returns (rows, columns)

# What does a row represent in this dataset?
# - A row is a reported ufo sighting

# What are the different ways missing values are encoded?
# Object columns
df.city.value_counts(dropna=False)  # No missing values here
df.shape_reported.value_counts(dropna=False)  # NaN are present
df.were_you_abducted.value_counts(dropna=False)  # - looks like a missing value
# Numeric columns
df.distance_reported.describe()  # -999 looks like a missing value encoding
df.distance_reported.isna().sum()  # 16 NaN in this column
df.estimated_size.isna().sum()  # No missing here

# How many np.nan in each column?
df.isna().sum()

# %%
#### Exercise 2 ####

# Shape reported replacing nan values with missing string
df.shape_reported.fillna("missing", inplace=True)
# Distance reported column replacing -999 values with nan value
df.distance_reported.replace(-999, np.nan, inplace=True)
# Imputing distance reported column with mean
df.distance_reported.fillna(df.distance_reported.mean(), inplace=True)
# Were you abducted replacing - with missing
df.were_you_abducted.replace("-", "missing", inplace=True)

# Printing first ten rows to paste in markdown
print(df.head(10).to_markdown())

# %%
#### Exercise 3 ####

# What is the median estimated size by shape, and mean distance reported by shape?
stats_table = (df.groupby("shape_reported")
               .agg(median_est_size=('estimated_size', 'median'),
                    mean_distance_reported=("distance_reported", 'mean'),
                    group_count=('were_you_abducted', 'count')))

# Printing table to markdown
print(stats_table.to_markdown())

# %%
#### Exercise 4 ####

# Changing all estimated size to sqft
cities_sqin = ["Holyoke", "Crater Lake", "Los Angeles", "San Diego", "Dallas"]

# Think of this as an if else statement
df = df.assign(estimated_size_sqft=np.where(df.city.isin(cities_sqin),  # Condition
                                                df.estimated_size / 144,  # If condition is true
                                                df.estimated_size))  # If condition is false

# Printing table to markdown
print(df.head(10).to_markdown())
