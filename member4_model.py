from sklearn.linear_model import LogisticRegression

def train_model(train):
    features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']

    X = train[features]
    y = train['Survived']

    model = LogisticRegression(max_iter=200)
    model.fit(X, y)

    print("Model trained successfully")
    return model