import pandas as pd

def load_data():
    train = pd.read_csv("Titanic_train.csv")
    test = pd.read_csv("Titanic_test.csv")

    print("Data Loaded Successfully")
    print("Train Shape:", train.shape)

    return train, test