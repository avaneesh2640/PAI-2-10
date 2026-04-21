import pandas as pd

def feature_engineering(train, test):

    # Clean text (important fix)
    train['Sex'] = train['Sex'].str.lower().str.strip()
    test['Sex'] = test['Sex'].str.lower().str.strip()

    # Convert categorical to numeric
    train['Sex'] = train['Sex'].map({'male': 0, 'female': 1})
    test['Sex'] = test['Sex'].map({'male': 0, 'female': 1})

    # Handle missing values
    train.fillna(0, inplace=True)
    test.fillna(0, inplace=True)

    return train, test