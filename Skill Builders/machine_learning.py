# %%
# Loading in packages
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# %%
# Loading in data
url = "../Data/machine_learning.csv"
df = pd.read_csv(url)

# Getting familiar with data
df.head()  # Taking a peek
df.dtypes  # What kind of data types do we have?
df.isna().sum()  # Any missing values?
df.describe()  # Summary statistics
df.survived.value_counts(normalize=True)  # Is there a class imbalance? Yes...

# %%
#### Exercise 1 ####
chart = px.histogram(df,
    x='age',
    y='survived',
    color='sex',
    title='Does age affect whether a passenger survived?',
    marginal="box", # or violin, rug
    hover_data=df.columns
)

chart.show()

# %%
#### Exercise 2 ####

# Step 0
X = df.drop("survived", axis=1)  # Drops the target column
y = df['survived']  # Selects the target columns

# %%
# Step 1
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                    random_state=24, stratify=y)
# %%
# Step 2
rf = RandomForestClassifier(random_state=24)  # Creating random forest object
rf.fit(X_train, y_train)  # Fit with the training data

# %%
# Step 3
y_pred = rf.predict(X_test)  # Using the features in the test set to make predictions

# %%
# Step 4
accuracy_score(y_test, y_pred)  # Comparing predictions to actual values

# %%
#### Exercise 3 ####
feat_imports = (pd.DataFrame({"feature names": X_train.columns,
                              "importances": rf.feature_importances_})
                .sort_values("importances", ascending=False))

print(feat_imports.to_markdown(index=False))

# %%
