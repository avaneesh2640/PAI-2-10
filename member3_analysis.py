import matplotlib.pyplot as plt

def analyze_data(df):
    print("\n===== DATA ANALYSIS =====")

    print("\nSurvival Count:")
    print(df["Survived"].value_counts())

    print("\nGender Count:")
    print(df["Sex"].value_counts())

    # Graph
    df["Survived"].value_counts().plot(kind="bar")
    plt.title("Survival Count")
    plt.xlabel("Survived (0 = No, 1 = Yes)")
    plt.ylabel("Count")
    plt.show()