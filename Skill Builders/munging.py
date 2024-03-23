# %%
# Loading modules
"""
Contains code that completes the Clean Movies skill builder. Note there are
many ways to accomplish the exercises! Spend time running each piece of code individually
and really understanding what's going on.
"""
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px

# %%
# Loading in data
url = "../Data/munging.csv"
df = pd.read_csv(url)

print(df.head(5).to_markdown(index=False))

# %%
#### Exercise 1 ####
# Splitting the column into two where the second column only contains the high range number.
# Print range_columns to see what this code did
range_columns = df.box_office_rev.str.split("- €", expand=True)

# Grabbing the second column and saving into our original dataframe with correct column name
# Changing data type to numeric! It was previously a string
df["high_range_rev"] = range_columns[1].astype(int)

# Dropping the old revenu column
df.drop("box_office_rev", axis=1, inplace=True)

print(df.head(5).to_markdown(index=False))

# %%
#### Exercise 2 ####
df['major_hit'] = np.where(df.major_hit == "yes", 1, 0)

print(df.head(5).to_markdown(index=False))

# %%
#### Exercise 3 ####

# Creating dictionary that maps rating to a number
ratings_dict = {
    "G": 0,
    "PG": 1,
    "PG-13": 2,
    "R": 3
}

# Using map method to convert the strings to their corresponding numbers and saving back into content_rating column
df["content_rating"] = df.content_rating.map(ratings_dict)

print(df.head(5).to_markdown(index=False))

# %%
#### Exercise 4 ####

# One hot encoding the genre column
df2 = pd.get_dummies(df, columns=["genre"])
# print(data2.head(5).to_markdown())

# %%
#### Exercise 5 ####

# Creating a fun graphic
# Using the five thirty eight theme
alt.themes.enable('fivethirtyeight')

# Getting the percentage of movies by rating
chart_data = df.content_rating.value_counts(normalize=True).reset_index()

# Chart specs
fig = px.bar(
    chart_data,  
    x='content_rating', 
    y='proportion', 
    title = 'Rated R movies are by far the most frequent'
)

fig.show()
