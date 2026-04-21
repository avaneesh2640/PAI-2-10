# member3_analysis.py

def analyze_data(train):
    print("\n--- Data Analysis ---")

    # Show first rows
    print("\nHead:")
    print(train.head())

    # Show info
    print("\nInfo:")
    print(train.info())

    # Show statistics
    print("\nDescribe:")
    print(train.describe())

    # Check missing values
    print("\nMissing Values:")
    print(train.isnull().sum())