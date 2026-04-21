import pandas as pd

# Load cleaned data (from Member 1 output)
train = pd.read_csv("train_clean.csv")
test = pd.read_csv("test_clean.csv")

# Convert categorical to numeric
train['Sex'] = train['Sex'].map({'male': 0, 'female': 1})
test['Sex'] = test['Sex'].map({'male': 0, 'female': 1})

# Convert Embarked column into numbers
train = pd.get_dummies(train, columns=['Embarked'], drop_first=True)
test = pd.get_dummies(test, columns=['Embarked'], drop_first=True)

# Select important features
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']

X = train[features]
y = train['Survived']

X_test = test[features]

# Save processed data
X.to_csv("X_train.csv", index=False)
y.to_csv("y_train.csv", index=False)
X_test.to_csv("X_test.csv", index=False)
print("Feature engineering done ✅")