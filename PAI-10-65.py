from sklearn.linear_model import LogisticRegression

def train_model(df):
    df = df.dropna()

    X = df[["Pclass", "Age", "Sex"]]
    y = df["Survived"]

    model = LogisticRegression()
    model.fit(X, y)

    print("Model Trained Successfully")

    return model