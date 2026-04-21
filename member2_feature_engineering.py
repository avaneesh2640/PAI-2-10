import pandas as pd

def feature_engineering(train, test):

    # Clean text
    train['Sex'] = train['Sex'].astype(str).str.lower().str.strip()
    test['Sex'] = test['Sex'].astype(str).str.lower().str.strip()

    # Convert categorical to numeric
    train['Sex'] = train['Sex'].map({'male': 0, 'female': 1}).astype(float)
    test['Sex'] = test['Sex'].map({'male': 0, 'female': 1}).astype(float)

    # Handle missing values
    train = train.fillna(0)
    test = test.fillna(0)

    return train, test