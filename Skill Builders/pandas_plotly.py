
#%%
import numpy as np
import pandas as pd
import plotly.express as px

#%%
url = 'https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/AER/Guns.csv'
df = pd.read_csv(url)
#%%
# 1.1 Using a line of code, select all the columns in this dfaset, assign it to a list called col_list

col_list = df.columns

# 1.2 `Using one line of code, show the number of columns and rows in df.`

df.shape

# `Just from looking at the output, what column(s) seems to be redundant with the row number?`

## unnamed:0 is redundant

# %%
# 2. Using a line of code, drop the column "Unnamed: 0" using the variable col_list
df = df.drop([col_list[0]], axis = 1)


#%%

# `what is the difference between exp1 and exp2?`
## exp1 is a bool value, while exp2 is a list of bool values

# `By putting df.violent < 300, and the violent column from df into a dfaframe, what is the relationship between the two columns?`
## df.violent<300 is the list evaulations of the expression according to df.violent. 

# Filter down the dfa set show that it only shows the dfa for idaho
df = df.query("state == 'Idaho'")

#%%
# Create a new column that show the ratio between murder rate and violent rate.
df.assign(ratio = df.murder/df.violent)

#%%
# Create a scatter plot that shows the relationship between murder rate and violent rate for the state of Idaho.
#     Your chart should show murder rate as the x-axis, violent as the y-axis.
mdf = df.query("state == 'Idaho'")

px.scatter(
    mdf,  
    x='murder', 
    y='violent', 
    title = "The Relationship Between Murder and Violence"
)

# %%
# Filter down the dfa set show that it only shows the dfa between 1993 and 1997
df.query("year >= 1993 and year <= 1997")

# Create a line chart that show prisoners numbers for the state of Idaho, Utah, and Oregon
# Your chart should show year as the x-axis, prisoner as the y-axis, along with a title
states = ["Idaho", "Utah", "Oregon"]

cdf = df.query("state in @states")

fig = px.line(
    cdf,  
    x='year', 
    y='prisoners', 
    color = 'state',
    title = 'Prisoner Number in the Three States'
)

fig.show()


#%%
# Without using query(), finshed exercise 2,5 and 7(jsut the wrangling). 
# 2
df[df.state == "Idaho"]
# 5
df[(df.year >= 1993) & (df.year<= 1997)]
# 6
df[df["state"].isin(["Idaho", "Utah", "Oregon"])]
