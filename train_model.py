# Using the linear regression model to get 
# data from a person and predict their clothing size
# independent(user data) and dependent variable (size)
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
df = pd.read_csv('body_measure.csv')

# Preprocess dataset
X = df[['Height', 'Weight', 'Waist', 'Hip']].values
y = pd.Categorical(df['Size'].replace({
    # reads the strings as integers
        'XS': 0,
        'S': 1,
        'M': 2,
        'L': 3,
        'XL': 4,
        'XXL': 5,
        'XXXL' : 6,
        '4XL' : 7,
        '5XL' : 8
}))

# Split dataset into training 
# and testing sets to evaluate performance of a model on new unseen data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train linear regression model on training set
reg = LinearRegression()
reg.fit(X_train, y_train)

# Evaluate performance of model on testing set
score = reg.score(X_test, y_test)
print('Model score:', score)

# Save model to file
joblib.dump(reg, 'model.pkl')
